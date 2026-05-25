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

## Concepts

### What is a Function?

A function is a reusable block of code that performs a specific task. Instead of writing the same code over and over, you define it once in a function and call it whenever you need it.

Think of it like a recipe with a name: "make_coffee()" -- every time you call it, the same steps execute.

```python
def greet(name):
    return f"Hello, {name}!"
```

Functions help you organize code, avoid repetition, and make programs easier to understand and debug.

### What are Parameters and Arguments?

- **Parameters** are the variable names in the function definition (placeholders).
- **Arguments** are the actual values you pass when calling the function.

```python
def add(a, b):       # a and b are parameters
    return a + b

add(3, 5)            # 3 and 5 are arguments
```

Python supports several argument types:
- **Positional**: matched by order
- **Keyword**: matched by name (`add(a=3, b=5)`)
- **Default**: have a fallback value (`def greet(name="World")`)
- **Variable-length**: `*args` (any number of positional) and `**kwargs` (any number of keyword)

### What is a Return Value?

A function can send a result back to the caller using `return`. Without it, the function returns `None` by default.

```python
def square(x):
    return x ** 2

result = square(4)  # result is 16
```

A function can return multiple values as a tuple: `return a, b, c`

### What is a Lambda Function?

A lambda is a small anonymous function written in a single line. It is useful for short operations you don't need to name.

```python
square = lambda x: x ** 2
```

Lambdas are commonly used with `map()`, `filter()`, and `sorted()` for quick transformations.

### What is Variable Scope?

Scope determines where a variable is accessible in your code:

- **Local scope**: variables created inside a function exist only within that function.
- **Global scope**: variables created outside all functions are accessible everywhere.
- **`global`** keyword: lets you modify a global variable from inside a function.
- **`nonlocal`** keyword: lets an inner function modify a variable from its enclosing function.

```python
x = 10          # global

def example():
    y = 5       # local -- only exists inside example()
    print(x)    # can READ global x
```

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
