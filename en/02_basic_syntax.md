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
