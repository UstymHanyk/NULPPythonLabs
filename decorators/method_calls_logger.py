import functools
import json

import os
from functools import wraps

def record_calls_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
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
