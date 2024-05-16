import os
from datetime import datetime
from typing import Optional

import psycopg2
import psycopg2.extras
from dotenv import load_dotenv

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
    conn = psycopg2.connect(**db_params)
    def wrapper(*args, **kwargs):
        try:
            return func(conn, *args, **kwargs)
        except Exception as e:
            print(e)
            conn.rollback()
        finally:
            conn.close()
    return wrapper