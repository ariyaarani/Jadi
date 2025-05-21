# Author: Mohammad Reza Arani

import time

def timing_decorator(n):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = n(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time}")
        return result
    return wrapper

@timing_decorator
def create_list(n):
    return list(range(1, n + 1))

my_list = create_list(10000000)
print(f"Number of items: {len(my_list)}")
