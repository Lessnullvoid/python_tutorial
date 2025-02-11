# Decorators in Python

import time
import functools

# Basic decorator
def timer(func):
    """A decorator that prints the execution time of a function"""
    @functools.wraps(func)  # Preserves function metadata
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds to run")
        return result
    return wrapper

# Decorator with arguments
def repeat(times):
    """A decorator that repeats a function a specified number of times"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

# Class decorator
def singleton(cls):
    """A decorator that ensures a class has only one instance"""
    instances = {}
    @functools.wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

# Example functions using decorators
@timer
def slow_function():
    """A function that simulates slow execution"""
    time.sleep(1)
    print("Slow function finished")

@repeat(times=3)
def greet(name):
    """Greet someone multiple times"""
    print(f"Hello, {name}!")

# Example class using decorator
@singleton
class DatabaseConnection:
    def __init__(self):
        self.connected = False
    
    def connect(self):
        if not self.connected:
            print("Connecting to database...")
            self.connected = True
        else:
            print("Already connected")

# Method decorator
class MyClass:
    def __init__(self):
        self.value = 0
    
    @property
    def doubled_value(self):
        """Property decorator example"""
        return self.value * 2
    
    @classmethod
    def from_string(cls, value_str):
        """Class method decorator example"""
        return cls(int(value_str))
    
    @staticmethod
    def validate(value):
        """Static method decorator example"""
        return isinstance(value, (int, float))

if __name__ == "__main__":
    # Testing timer decorator
    print("Testing timer decorator:")
    slow_function()
    
    # Testing repeat decorator
    print("\nTesting repeat decorator:")
    greet("Alice")
    
    # Testing singleton decorator
    print("\nTesting singleton decorator:")
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()
    print(f"Same instance? {db1 is db2}")
    db1.connect()
    db2.connect()
    
    # Testing method decorators
    print("\nTesting method decorators:")
    obj = MyClass()
    obj.value = 5
    print(f"Doubled value: {obj.doubled_value}")
    print(f"Is 42 valid? {MyClass.validate(42)}")
    print(f"Is 'hello' valid? {MyClass.validate('hello')}") 