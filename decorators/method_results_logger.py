import functools

def write_result_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open(f"{args[0].__class__.__name__}_{func.__name__}.txt", "a") as f:
            f.write(str(result) + "\n")
        return result
    return wrapper
