# cache
cache_data = {}


# cache decorator (if have already counted value in cache - then take value from cache, else - count)
def cache(func):
    def wrapper(argument):
        global cache_data
        key = argument
        if key in cache_data:
            return cache_data[key]
        else:
            result = func(argument)
            cache_data[key] = result
            return result
    return wrapper


# fibonacci function
@cache
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# calling func for test
print(cache_data)
print(fibonacci(5))  # The calculation is performed
print(cache_data)
print(fibonacci(5))  # The result from the cache is used
print(cache_data)
print(fibonacci(3))  # The calculation is performed
print(cache_data)
print(fibonacci(14))  # The result from the cache is used
print(cache_data)
print(fibonacci(3))  # The result from the cache is used
