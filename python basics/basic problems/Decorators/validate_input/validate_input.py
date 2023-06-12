# this decorator will check if all inputs are float or int, otherwise it will throw an error
def validate_input(func):
    def wrapper(*args, **kwargs):
        for el in args:
            if type(el) != type(1) and type(el) != type(1.0):
                raise ValueError('there non-number argument.')
        for el in kwargs.values():
            if type(el) != type(1) and type(el) != type(1.0):
                raise ValueError('there non-number argument.')
        return func(*args, **kwargs)

    return wrapper


# creating func with decoratore
@validate_input
def multiply(*args, **kwargs):
    product = 1
    for el in args:
        product *= el
    for el in kwargs.values():
        product *= el
    return product


# some test
print(multiply(5, 10))
print(multiply(3, 4, 5, a=10, b=11, c=12))
print(multiply(1, 2, 3, '1'))
