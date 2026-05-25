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

## Concepts

### What is a Decorator?

A decorator is a function that takes another function as input and extends or modifies its behavior without changing its source code. It "wraps" the original function with additional logic.

Think of it like gift wrapping: the gift (original function) stays the same, but the wrapper adds something extra (logging, timing, access control, etc.).

```python
@timer
def slow_function():
    ...
```

The `@timer` syntax is shorthand for: `slow_function = timer(slow_function)`. Decorators are widely used in web frameworks, testing, and performance monitoring.

### What is a Context Manager?

A context manager is an object that automatically sets up and tears down resources (files, database connections, locks, etc.). You use it with the `with` statement.

```python
with open("file.txt") as f:
    data = f.read()
# file is automatically closed here, even if an error occurred
```

Without a context manager, you would need to manually close resources and handle errors -- easy to forget and a common source of bugs.

You can create your own by implementing `__enter__` and `__exit__` methods or by using `@contextmanager` from the `contextlib` module.

### What is a Generator?

A generator is a function that produces a sequence of values lazily -- one at a time, on demand -- instead of computing them all at once and storing them in memory. It uses `yield` instead of `return`.

```python
def count_up(n):
    i = 0
    while i < n:
        yield i
        i += 1
```

When you call a generator function, it doesn't run immediately. It returns a generator object that produces values one by one each time you ask for the next one (with `next()` or a `for` loop).

Generators are essential when working with large datasets or infinite sequences because they only use memory for one value at a time.

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
