# Polymorphism in Python

from abc import ABC, abstractmethod

# Abstract base class
class Shape(ABC):
    """Abstract base class for shapes"""
    
    @abstractmethod
    def area(self):
        """Calculate area of the shape"""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Calculate perimeter of the shape"""
        pass
    
    def describe(self):
        """Describe the shape"""
        return f"This is a {self.__class__.__name__}"

# Concrete classes implementing Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius

# Duck typing example
class Duck:
    def make_sound(self):
        return "Quack!"
    
    def swim(self):
        return "Swimming like a duck"

class Person:
    def make_sound(self):
        return "Hello!"
    
    def swim(self):
        return "Swimming like a person"

# Function demonstrating duck typing
def make_it_swim_and_sound(thing):
    """This function works with any object that has make_sound and swim methods"""
    print(thing.make_sound())
    print(thing.swim())

# Method overloading through default arguments
class Calculator:
    def add(self, x, y=0, z=0):
        return x + y + z

# Operator overloading
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __len__(self):
        return 2  # 2D vector

if __name__ == "__main__":
    # Demonstrating polymorphism with inheritance
    shapes = [Rectangle(5, 3), Circle(4)]
    print("Shape calculations:")
    for shape in shapes:
        print(f"\n{shape.describe()}")
        print(f"Area: {shape.area():.2f}")
        print(f"Perimeter: {shape.perimeter():.2f}")
    
    # Demonstrating duck typing
    print("\nDuck typing:")
    objects = [Duck(), Person()]
    for obj in objects:
        make_it_swim_and_sound(obj)
    
    # Demonstrating method overloading
    print("\nMethod overloading:")
    calc = Calculator()
    print(f"Add two numbers: {calc.add(5, 3)}")
    print(f"Add three numbers: {calc.add(5, 3, 2)}")
    
    # Demonstrating operator overloading
    print("\nOperator overloading:")
    v1 = Vector(2, 3)
    v2 = Vector(3, 4)
    v3 = v1 + v2
    print(f"Vector addition: {v3}")
    print(f"Vector length: {len(v1)}") 