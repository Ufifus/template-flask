# Flask Template Project

This repository contains a template for a Flask project, including configurations for development and production
environments, logging, error handling, and a structured application setup with blueprints.

## Table of Contents

- [Getting Started](#getting-started)
- [Configuration](#configuration)
- [Development](#development)
- [Production](#production)

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

- Python 3.10
- pip (Python package installer)

### Installation

1. Clone the repo
    ```sh
    git clone https://github.com/yourusername/your-repo.git
    cd your-repo
    ```

2. Create and activate a virtual environment
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies
    ```sh
    pip install -r requirements.txt
    ```

## Configuration

The application configuration is managed using environment variables. Create a `.env` file in the root directory to
specify these variables.

- `HOST`: The host address for the Flask application
- `PORT`: The port for the Flask application
- `DEBUG`: Enable/disable debug mode (default: `True`)
- `DB_HOST`: The host address for the database
- `DB_NAME`: The name of the database
- `DB_USER`: The database user
- `DB_PASSWORD`: The database password
- `DB_PORT`: The database port

## Development

To run the application in development mode, use the following command:

```sh
python main.py
```

This will start the Flask application with the settings specified in your .env file.

## Production

To run the application in production mode, use gunicorn. It is a Python WSGI HTTP Server for UNIX.

```sh
gunicorn -w 4 --bind 127.0.0.1:8080 'wsgi:create_app'
```

This command starts the application with 4 worker processes, binding to the specified address and port.

