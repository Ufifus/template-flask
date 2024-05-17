class CustomError(Exception):
    def __init__(self, message: str = '', code: int = 500):
        """
        Custom error class for handling application-specific errors.

        :param message: Error message
        :param code: HTTP status code
        """
        self.message = message
        self.code = code
