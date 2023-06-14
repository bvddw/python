def log_decorator(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            with open(filename, 'a') as file:
                file.write(f'Function: {func.__name__}, Arguments: {args, kwargs}, Result: {func(*args, **kwargs)}\n')
        return wrapper
    return decorator


@log_decorator('log.txt')
def add_numbers(a, b):
    return a + b


@log_decorator('log.txt')
def multiply_numbers(a, b):
    return a * b


add_numbers(2, 3)
multiply_numbers(4, 5)
