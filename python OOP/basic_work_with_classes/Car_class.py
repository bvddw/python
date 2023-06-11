class Car:
    def __init__(self, brand_: str, model_: str, year_: int, speed_: float, max_speed_: float) -> None:
        self.brand = brand_
        self.model = model_
        self.year = year_
        self.speed = speed_
        self.max_speed = max_speed_

    def __str__(self) -> str:
        return f'Brand: {self.brand}, Model: {self.model}, year: {self.year}, speed now: {self.speed} km/h, max. speed: {self.max_speed} km/h.'

    def acceleration(self, speed_: float):
        self.speed += speed_

    def slowdown(self, speed_: float):
        self.speed -= speed_


brand: str = input('Enter the brand of your car: ')
model: str = input('Enter the model of your car: ')
while True:
    try:
        year: int = int(input('Enter the year of manufacture of the machine: '))
        break
    except ValueError:
        print('You need to enter the integer number.')
while True:
    try:
        speed: float = float(input('Enter current speed: '))
        break
    except ValueError:
        print('You need to enter the float number.')
while True:
    try:
        max_speed: float = float(input('Enter the maximum speed: '))
        break
    except ValueError:
        print('You need to enter the float number.')
car: Car = Car(brand, model, year, speed, max_speed)
while True:
    try:
        choice: int = int(input('''1 - Increase a speed
2 - Slow down
3 - Check car data
4 - Exit program\n'''))
        match choice:
            case 1:
                while True:
                    try:
                        add_speed: float = float(input('How much do you want to speed up? '))
                        break
                    except ValueError:
                        print('You need to enter float number.')
                if car.speed + add_speed > car.max_speed:
                    print('We cannot ride that fast.')
                else:
                    car.acceleration(add_speed)
            case 2:
                while True:
                    try:
                        sub_speed: float = float(input('How much do you want to slow down? '))
                        break
                    except ValueError:
                        print('You need to enter float number.')
                if car.speed + sub_speed < 0:
                    print('We cannot ride that slow.')
                else:
                    car.acceleration(sub_speed)
            case 3:
                print(car)
            case 4:
                print('Program Finished.')
                break
            case _:
                print('Incorrect data.')
    except ValueError:
        print('You need to enter integer number.')
