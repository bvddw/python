def validate_age(minimum_age):
    def decorator(cls):
        original_init = cls.__init__

        def new_init(self, name, age):
            if age < minimum_age:
                raise ValueError('Not enough age.')
            original_init(self, name, age)

        cls.__init__ = new_init
        return cls

    return decorator


@validate_age(minimum_age=18)
class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __str__(self):
        return f'Name: {self.name}, age: {self.age}.'


try:
    human1: Person = Person('Bob', 18)
except ValueError:
    print('Not enough age.')
else:
    print(human1)
try:
    human2: Person = Person('Jack', 12)
except ValueError:
    print('Not enough age.')
else:
    print(human2)
