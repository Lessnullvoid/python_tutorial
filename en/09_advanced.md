# Advanced Python Concepts (Section 09)

This section explores advanced Python features and programming techniques.

## Code Description

- [`context_managers.py`](../09_advanced/context_managers.py): Shows how to implement context managers for efficient resource handling.
- [`decorators.py`](../09_advanced/decorators.py): Demonstrates the use of decorators to modify the behavior of functions and classes.
- [`generators.py`](../09_advanced/generators.py): Illustrates the use of generators and iterators for efficient data sequence handling.

## Section Contents

In this section we will cover:
1. **Decorators**: Modifying function behavior.
2. **Context Managers**: Efficient resource management with `with`.
3. **Generators and Iterators**: Creating sequences and data streams.

## Detailed Code Description

### context_managers.py
This file shows how to implement **context managers** in Python.

**Code examples:**
```python
class Timer:
    def __enter__(self):
        self.start = time.time()
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Duration: {time.time() - self.start:.2f} seconds")
```
```python
@contextmanager
def temporary_attribute(obj, name, value):
    original = getattr(obj, name, None)
    setattr(obj, name, value)
    yield
    setattr(obj, name, original)
```

### decorators.py
This file introduces the use of **decorators in Python**.

**Code examples:**
```python
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time() - start:.4f} seconds")
        return result
    return wrapper
```
```python
def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance
```

### generators.py
This file shows how to use **generators and iterators in Python**.

**Code examples:**
```python
def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
```
```python
def infinite_counter():
    num = 0
    while True:
        yield num
        num += 1
```
```python
def echo_generator():
    while True:
        received = yield
        print(f"Received: {received}")
```

## How to Run the Programs

1. Make sure Python is installed on your machine.
2. Navigate to the project directory in your terminal.
3. Use the command line to run a program. For example:
   ```bash
   python 09_advanced/decorators.py
   ```
