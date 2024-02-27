class Shape:
    def get_area(self):
        raise NotImplementedError("Subclasses must implement get_area()")

    def set_dimensions(self, width, height):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14 * self.radius**2

    def set_dimensions(self, radius, _):
        self.radius = radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def set_dimensions(self, width, height):
        self.width = width
        self.height = height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def get_area(self):
        return 0.5 * self.base * self.height

#added subclass polygon with multiple sides
class Polygon(Shape):
    def __init__(self, sides_length):
        self.sides_length = sides_length

    def get_area(self):
        return sum(self.sides_length) * 2 #generic polygon

    def set_dimensions(self, _, __):
        pass

#print original area
def print_area(shape):
    print(f"Area of {type(shape).__name__}: {shape.get_area()}")

#set dimensions and print modified area
def set_dimensions_and_print_area(shape, width, height):
    shape.set_dimensions(width, height)
    print(f"Modified area of {type(shape).__name__}: {shape.get_area()}")

def main():
    circle = Circle(radius=3)
    rectangle = Rectangle(width=3, height=3)
    triangle = Triangle(base=3, height=3)
    polygon = Polygon(sides_length=[3, 3, 3, 3])

    shapes = [circle, rectangle, triangle, polygon]

    for shape in shapes:
        print_area(shape)
        set_dimensions_and_print_area(shape, 2, 2)

if __name__ == "__main__":
    main()

#The base class Shape provides the get_area method as well as the
#placeholder method set_dimensions for handling differences in setting dimensions
#each subclass implements the get_area method based on its specific calculation
#and the set_dimensions method if needed