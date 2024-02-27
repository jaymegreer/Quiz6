from abc import ABC, abstractmethod

class Shape(ABC): #base class
    @abstractmethod
    def get_area(self):
        pass

class Circle(Shape): #concrete
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14 * self.radius**2

class Square(Shape): #concrete
    def __init__(self, side_length):
        self.side_length = side_length

    def get_area(self):
        return self.side_length**2

class Rectangle(Shape): #concrete
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

#new shape without changing existing code - triangle
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def get_area(self):
        return self.base * self.height / 2


def main():
    radius = 3
    side = 3
    length = 3
    width = 3
    base = 3
    height = 3

    circle = Circle(radius)
    square = Square(side)
    rectangle = Rectangle(length, width)
    triangle = Triangle(base, height)

    print(circle.get_area())
    print(square.get_area())
    print(rectangle.get_area())
    print(triangle.get_area())

if __name__ == "__main__":
    main()
