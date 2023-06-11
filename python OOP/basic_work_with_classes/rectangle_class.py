class Rectangle:
    def __init__(self, length: float, width: float) -> None:
        self.length = length
        self.width = width

    def __str__(self) -> str:
        return f'length: {self.length}, width: {self.width}, perimeter: {self.get_perimeter()}, square: {self.get_square()}.'

    def get_perimeter(self) -> float:
        return 2 * (self.width + self.length)

    def get_square(self) -> float:
        return self.length * self.width


while True:
    try:
        length_ = float(input('Enter length: '))
        break
    except ValueError:
        print('You need to enter float number.')

while True:
    try:
        width_ = float(input('Enter width: '))
        break
    except ValueError:
        print('You need to enter float number.')

rectangle: Rectangle = Rectangle(length_, width_)
print(rectangle)
