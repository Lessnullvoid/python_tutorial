"""
Main functionality of the package
"""

def greet(name):
    """Simple greeting function"""
    return f"Hello, {name}!"

class Calculator:
    """A simple calculator class"""
    
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def subtract(a, b):
        return a - b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b 