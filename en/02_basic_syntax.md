# Python Basic Syntax (Section 02)

This section covers fundamental Python syntax and basic programming concepts.

## Code Description

- [`variables.py`](../02_basic_syntax/variables.py): Demonstrates variable declaration, assignment, and usage in Python.
- [`operators.py`](../02_basic_syntax/operators.py): Illustrates the use of arithmetic, comparison, and logical operators with examples.
- [`comments.py`](../02_basic_syntax/comments.py): Shows how to write single-line and multi-line comments in Python.
- [`input_output.py`](../02_basic_syntax/input_output.py): Provides examples of using `input()` for user input and `print()` for displaying results.

## Learning Objectives

By the end of this section, you should be able to:
1. Declare and use variables in Python.
2. Understand and apply different types of operators.
3. Write effective comments in your code.
4. Handle input and output in Python programs.

## Concepts

### What is a Variable?

A variable is a named container that stores a value in your computer's memory. Think of it as a labeled box: you put something inside (a number, text, etc.) and later refer to it by name.

In Python, you create a variable by simply assigning a value with `=`:

```python
age = 25
name = "Alice"
```

You don't need to declare the type -- Python figures it out automatically.

### What are Data Types?

Every value in Python has a type that determines what you can do with it:

- **int** -- whole numbers: `42`, `-7`, `0`
- **float** -- decimal numbers: `3.14`, `-0.5`
- **str** -- text (strings): `"hello"`, `'world'`
- **bool** -- True or False values: `True`, `False`

Python is dynamically typed, meaning a variable can change its type if you reassign it.

### What are Operators?

Operators are symbols that perform operations on values:

- **Arithmetic**: `+`, `-`, `*`, `/`, `%` (remainder), `**` (power), `//` (integer division)
- **Comparison**: `==`, `!=`, `>`, `<`, `>=`, `<=` -- these return True or False
- **Logical**: `and`, `or`, `not` -- combine or invert boolean values
- **Assignment**: `=`, `+=`, `-=`, `*=`, `/=` -- store or update values

### What are Comments?

Comments are notes in your code that Python ignores completely. They exist only for humans reading the code. Use them to explain WHY something is done (not what -- the code shows that).

```python
# single-line comment

"""
Multi-line comment (docstring)
used for longer explanations.
"""
```

### What is Input/Output?

- **Output** (`print()`): displays information to the user on screen.
- **Input** (`input()`): pauses the program and waits for the user to type something, then returns what they typed as a string.

```python
answer = input("What is your name? ")  # waits for user
print(f"Hello, {answer}!")             # shows result
```

## Detailed Code Description

### variables.py
This file introduces the use of **variables and data types in Python**. It includes examples on how to declare and assign variables, as well as how to check their types.

**Code examples:**
```python
name = "John Doe"  # String
age = 25           # Integer
height = 1.75      # Float
is_student = True  # Boolean
```

### operators.py
This file shows how to use **operators in Python**, including arithmetic, comparison, logical, and assignment operators.

**Code examples:**
```python
a = 10
b = 3
print(a + b, a - b, a * b, a / b, a % b)
```

### comments.py
This file explains how to write **comments in Python** to document and organize your code.

**Code examples:**
```python
# This is a single-line comment
"""
This is a multi-line comment
that serves as documentation.
"""
```

### input_output.py
This file illustrates how to handle **input and output in Python** using `input()` to read data from the user and `print()` to display results.

**Code examples:**
```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hello, {name}! Next year, you will be {age + 1}.")
```

## How to Run the Programs

1. Make sure Python is installed on your machine.
2. Open a terminal or command prompt.
3. Navigate to the project directory.
4. Run a program with the command: `python 02_basic_syntax/filename.py`, replacing `filename.py` with the name of the file you want to run (for example, `python 02_basic_syntax/variables.py`).
