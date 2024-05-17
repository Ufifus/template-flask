"""
This module sets up and configures the Flask application, including loading
environment variables, applying configuration settings from the `Config` class,
registering Flask blueprints, setting up Cross-Origin Resource Sharing (CORS),
and configuring application logging.
"""
import logging
import sys

from flask import Flask
from flask_cors import CORS

from api import child_app, Config


def create_app():
    """
    Главное приложение для запуска сервера,
    здесь прописываются настройки запуска и так же связываются дочерние проекты с главным
    """
    app = Flask(__name__, static_url_path='')
    app.config.from_object(Config)

    # Register blueprints
    app.register_blueprint(child_app)

    # Configure CORS with default settings
    CORS(app, resources={r"/*": {"origins": "*"}})

    # Logging configuration
    logging.basicConfig(level=logging.DEBUG)

    # Console handler for all log levels
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.DEBUG)
    console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(console_formatter)
    logging.getLogger().addHandler(console_handler)

    # File handler for critical errors
    file_handler = logging.FileHandler('CRITICAL.log')
    file_handler.setLevel(logging.CRITICAL)
    file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_formatter)
    logging.getLogger().addHandler(file_handler)

    return app


if __name__ == '__main__':
    flask_app = create_app()
    flask_app.logger.info('-----------------')
    flask_app.logger.info('Starting on address %s:%s...',
                          flask_app.config["HOST"],
                          flask_app.config["PORT"])

    flask_app.run(debug=flask_app.config['DEBUG'],
                  host=flask_app.config['HOST'],
                  port=flask_app.config['PORT'])
