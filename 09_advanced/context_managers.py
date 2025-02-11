# Context Managers in Python

import time
from contextlib import contextmanager

# Class-based context manager
class Timer:
    """A context manager for timing code execution"""
    
    def __init__(self, description):
        self.description = description
    
    def __enter__(self):
        self.start = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        self.duration = self.end - self.start
        print(f"{self.description}: {self.duration:.2f} seconds")

# Function-based context manager using decorator
@contextmanager
def temporary_attribute(obj, name, value):
    """Temporarily set an attribute on an object"""
    original = getattr(obj, name, None)
    setattr(obj, name, value)
    try:
        yield
    finally:
        if original is None:
            delattr(obj, name)
        else:
            setattr(obj, name, original)

# Custom file context manager
class OpenFile:
    """A custom context manager for file handling"""
    
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        # Handle specific exceptions
        if exc_type is FileNotFoundError:
            print(f"Error: File {self.filename} not found")
            return True  # Suppress the exception

# Nested context manager example
@contextmanager
def managed_resources(*managers):
    """Manage multiple context managers"""
    exits = []
    values = []
    try:
        for mgr in managers:
            mgr_enter = mgr.__enter__()
            exits.append(mgr.__exit__)
            values.append(mgr_enter)
        yield values
    finally:
        for exit_func in reversed(exits):
            exit_func(None, None, None)

if __name__ == "__main__":
    # Using Timer context manager
    print("Using Timer context manager:")
    with Timer("Sleep operation"):
        time.sleep(1)
    
    # Using temporary_attribute
    print("\nUsing temporary_attribute:")
    class Person:
        def __init__(self, name):
            self.name = name
    
    person = Person("Alice")
    print(f"Original name: {person.name}")
    with temporary_attribute(person, 'name', 'Bob'):
        print(f"Temporary name: {person.name}")
    print(f"Back to original: {person.name}")
    
    # Using custom file handler
    print("\nUsing custom file handler:")
    with OpenFile("example.txt", "w") as file:
        file.write("Hello, World!")
    
    # Using nested context managers
    print("\nUsing nested context managers:")
    timer1 = Timer("Operation 1")
    timer2 = Timer("Operation 2")
    
    with managed_resources(timer1, timer2) as (t1, t2):
        time.sleep(0.5)  # First operation
        time.sleep(0.3)  # Second operation 