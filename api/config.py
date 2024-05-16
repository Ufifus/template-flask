"""
This module is responsible for defining the configuration settings for the application.
It loads environment variables from a .env file if present and sets up default values
for various configuration options, such as the server host and port.
"""
import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """
    The Config class stores configuration settings for the application.
    These settings include the server host, port, debug mode, and any other
    application-specific configurations that may be controlled via environment variables.
    """

    HOST = os.getenv('HOST', '127.0.0.1')
    PORT = int(os.getenv('PORT', '5000'))
    DEBUG = True  # Set to False in production
    # Add other configurations here
