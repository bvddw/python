def count_calls(cls):
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.instance = cls(*args, **kwargs)
            self.call_count = {}

        def __getattr__(self, name):
            attr = getattr(self.instance, name)
            if callable(attr):
                return self._wrap_method(attr)
            return attr

        def _wrap_method(self, method):
            def wrapper(*args, **kwargs):
                self._increment_call_count(method.__name__)
                return method(*args, **kwargs)
            return wrapper

        def _increment_call_count(self, method_name):
            if method_name not in self.call_count:
                self.call_count[method_name] = 1
            else:
                self.call_count[method_name] += 1

    return Wrapper


@count_calls
class MyClass:
    def method1(self):
        pass

    def method2(self):
        pass

    def method3(self):
        pass


obj = MyClass()

obj.method1()
obj.method2()
obj.method1()
obj.method3()

print(obj.call_count)
