import datetime
file = open('check.txt', 'w')


# creating a decorator that will write information about the function we called to a file
def logger(func):
    def wrapper(*args, **kwargs):
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f'[{now_time}] Function {func.__name__} called with arguments: {args}, {kwargs}\n')
        return func(*args, **kwargs)
    return wrapper


# creating function
@logger
def add(a, b):
    return a + b


# calling for test
add(3, 5)
add(2, 4)
file.close()
