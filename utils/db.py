import logging
import os

import psycopg2
import psycopg2.extras
from dotenv import load_dotenv
from flask import jsonify
from sshtunnel import SSHTunnelForwarder

from .errors import CustomError
from .logger import logger

# Load environment variables
load_dotenv()

db_params = {
    'host': os.getenv("DB_HOST"),
    'database': os.getenv("DB_NAME"),
    'user': os.getenv("DB_USER"),
    'password': os.getenv("DB_PASSWORD"),
    'port': os.getenv("DB_PORT"),
}

def db_decorator(func):
    def wrapper(*args, **kwargs):
        # Manage database connections within the decorator to avoid persistent connections.
        tunnel = None
        if int(os.getenv("SSH_USE")):
            # Create an SSH tunnel
            tunnel = SSHTunnelForwarder(
                ('158.160.16.124', 22),
                ssh_username='maintenance',
                ssh_pkey=os.getenv("SSH_PRIVATE_KEY"),
                remote_bind_address=('127.0.0.1', 5432),
                local_bind_address=('localhost', int(os.getenv('SSH_ALLOWED_PORT'))),  # could be any available port
            )
            # Start the tunnel
            try:
                tunnel.start()
            except Exception as e:
                logger.error("SSH ERROR: Non connected because " + str(e))
                tunnel.quit()
                return jsonify({'error': "SSH ERROR: Non connected because " + str(e)}), 500

            # Create a database connection
            conn = psycopg2.connect(
                database=os.getenv("SSH_DB_NAME"),
                user=os.getenv("SSH_DB_USER"),
                password=os.getenv("SSH_DB_PASSWORD"),
                host=tunnel.local_bind_host,
                port=tunnel.local_bind_port
            )
        else:
            conn = psycopg2.connect(**db_params)
        try:
            return func(conn, *args, **kwargs)
        except CustomError as e:
            logger.error('Database error: %s', e.message)
            conn.rollback()
            return jsonify({'error': e.message}), e.code
        except Exception as e:
            logger.exception('Unexpected error: %s', e)
            conn.rollback()
            return jsonify({'error': 'Internal server error'}), 500
        finally:
            conn.close()
            if tunnel:
                tunnel.stop()
            logger.debug('Database connection closed')

    return wrapper
