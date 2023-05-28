import os
import subprocess

def run_pylint(file_name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            runner = f"py -m pylint {os.path.abspath(file_name)}"
            subprocess.run(runner, shell=True)
            return func(*args, **kwargs)
        return wrapper
    return decorator
