from functools import wraps


def logWrapper(logger):
    def _decorator(func):
        @wraps(func)
        def _wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return _wrapper

    return _decorator
