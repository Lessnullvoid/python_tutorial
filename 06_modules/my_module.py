"""
A simple example module to demonstrate module creation and usage.
This module contains basic mathematical operations and utilities.
"""

# Module level variables
PI = 3.14159
GRAVITY = 9.81

# Basic mathematical functions
def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide a by b"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# A simple class definition
class Circle:
    """A class to represent a circle"""
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        """Calculate the area of the circle"""
        return PI * self.radius ** 2
    
    def circumference(self):
        """Calculate the circumference of the circle"""
        return 2 * PI * self.radius

# Private function (with underscore)
def _internal_function():
    """This is an internal function not meant to be used directly"""
    pass

# Example usage when run as a script
if __name__ == "__main__":
    print("Testing the module...")
    print(f"Adding 5 + 3 = {add(5, 3)}")
    circle = Circle(5)
    print(f"Circle area with radius 5: {circle.area():.2f}") 