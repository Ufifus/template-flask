import logging
import os

import psycopg2
import psycopg2.extras
from dotenv import load_dotenv
from flask import jsonify

from .errors import CustomError

logger = logging.getLogger(__name__)

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
        conn = psycopg2.connect(**db_params)
        try:
            logger.debug('Database connection established')
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
            logger.debug('Database connection closed')

    return wrapper
