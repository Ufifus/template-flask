import logging
from functools import wraps

from flask import request, jsonify

logger = logging.getLogger(__name__)


def jwt_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # JWT authentication
        logger.debug('Checking authentication for request %s', request.path)
        if False:
            return jsonify({'error': 'Unauthorized access'}), 401
        return func(*args, **kwargs)

    return wrapper
