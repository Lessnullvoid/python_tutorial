# Functions in Python (Section 05)

This section explores function definition, arguments, and advanced function concepts.

## Code Description

- [`basic_functions.py`](../05_functions/basic_functions.py): Introduces the syntax for defining basic functions.
- [`arguments_returns.py`](../05_functions/arguments_returns.py): Shows the use of positional arguments, keyword arguments, and multiple return values.
- [`lambda_functions.py`](../05_functions/lambda_functions.py): Provides examples of lambda functions and their practical usage.
- [`scope_examples.py`](../05_functions/scope_examples.py): Explains variable scope in Python, including `global` and `nonlocal`.

## Learning Objectives
1. Define and call functions in Python.
2. Understand and use different types of function arguments.
3. Return values from functions effectively.
4. Create and use lambda functions.
5. Understand the scope of local and global variables.

## Detailed Code Description

### basic_functions.py
This file introduces the definition and use of **basic functions in Python**.

**Code examples:**
```python
def greet():
    print("Hello, World!")

def add_numbers(a, b):
    return a + b
```

### arguments_returns.py
This file shows how to work with **different types of arguments and return values in functions**.

**Code examples:**
```python
def print_info(name, age, city):
    print(f"Name: {name}, Age: {age}, City: {city}")

def sum_all(*args):
    return sum(args)
```

### lambda_functions.py
This file introduces **lambda functions (anonymous functions)** and how they are used in combination with `map()`, `filter()`, and `sorted()`.

**Code examples:**
```python
square = lambda x: x**2
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, numbers))
```

### scope_examples.py
This file explains the concept of **variable scope in Python**.

**Code examples:**
```python
global_var = "I am global"
def demonstrate_scope():
    local_var = "I am local"
    print(local_var)
    print(global_var)
```
```python
def outer_function():
    outer_var = "Outer"
    def inner_function():
        nonlocal outer_var
        outer_var = "Modified"
```

## How to Run the Programs

1. Make sure Python is installed on your machine.
2. Navigate to the project directory.
3. Use the command line to run a specific program. For example:
   ```bash
   python 05_functions/basic_functions.py
   ```
