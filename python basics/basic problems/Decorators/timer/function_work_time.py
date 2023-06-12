import time
import timeit


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = timeit.default_timer()
        func(*args, **kwargs)
        end_time = timeit.default_timer()
        execution_time = end_time - start_time
        with open('time.txt', 'a') as file:
            file.write('Function completed.\n')
            file.write(f'Execution time: {execution_time} seconds.\n')
    return wrapper


@timer
def my_function():
    time.sleep(2)
    print("Function completed")


my_function()
