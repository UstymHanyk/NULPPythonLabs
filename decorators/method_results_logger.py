from functools import wraps

def write_result_decorator(func):
    """
    Decorator that writes the result of a function to a text file.

    Args:
        func (function): The function to be decorated.

    Returns:
        function: The decorated function.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        Wrapper function that executes the decorated function and writes the result to a file.

        Args:
            *args: Positional arguments passed to the decorated function.
            **kwargs: Keyword arguments passed to the decorated function.

        Returns:
            The  result of the decorated function.
        """

        result = func(*args, **kwargs)
        with open(f"{args[0].__class__.__name__}_{func.__name__}.txt", "a") as f:
            f.write(str(result) + "\n")
        return result
    return wrapper

