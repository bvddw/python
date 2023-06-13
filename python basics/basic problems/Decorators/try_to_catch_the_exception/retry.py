# decorator will try to restart function to complete this in case exception
def retry(max_attempts):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f'Got the exception {e}. Retrying...')
                    attempts += 1
            print('Reached maximum attempts. No more retries.')

        return wrapper

    return decorator


# creating func with possible exception
@retry(max_attempts=3)
def divide(a, b):
    return a / b


# some calls
result = divide(10, 2)
print(result)  # Output: 5.0

result = divide(10, 0)
print(result)  # Output: Three times we got exception and after this return None
