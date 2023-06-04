import os
from functools import wraps

def record_calls_decorator(func):
    """
    Decorator that records the number of calls made to a function in a text file.

    Args:
        func (function): The function to be decorated.

    Returns:
        function: The decorated function.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        Wrapper function that executes the decorated function and updates the call count in a file.

        Args:
            *args: Positional arguments passed to the decorated function.
            **kwargs: Keyword arguments passed to the decorated function.

        Returns:
            The result of the decorated function.
        """
        file_path = "../manager/method_calls.txt"
        call_count = 0
        if os.path.exists(file_path):
            with open(file_path, "r+") as f:
                for line in f:
                    if func.__name__ in line:
                        call_count = int(line.split(":")[1])
                        break
                else:
                    f.write(f"\n{func.__name__}:0")

        with open(file_path, "r") as f:
            lines = f.readlines()

        with open(file_path, "w") as f:
            for line in lines:
                if func.__name__ in line:
                    call_count += 1
                    f.write(f"{func.__name__}:{call_count}\n")
                else:
                    f.write(line)
        return func(*args, **kwargs)

    return wrapper
