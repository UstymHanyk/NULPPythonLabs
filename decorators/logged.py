import logging


def logged(exception, mode):
    """
    Logged decorator.

    Decorator that logs the exception raised by a decorated method.

    Args:
        exception (Exception): The exception to be logged.
        mode (str): The logging mode ("console" or "file").
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception as e:
                logger = logging.getLogger(__name__)
                if mode == "console":
                    handler = logging.StreamHandler()
                elif mode == "file":
                    handler = logging.FileHandler("log.txt")
                else:
                    raise ValueError("Invalid logging mode. Choose either 'console' or 'file'.")
                logger.addHandler(handler)
                logger.setLevel(logging.INFO)
                logger.exception(str(e))
        return wrapper
    return decorator
