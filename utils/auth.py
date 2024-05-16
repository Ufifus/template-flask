def jwt_decorator(func):
    def wrapper(*args, **kwargs):
        print('checking auth')
        return func(*args, **kwargs)
    return wrapper