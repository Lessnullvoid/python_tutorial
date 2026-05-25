# Introduction to Python Programming

This section covers the basics of Python programming.

## Contents
1. "Hello World" program
2. Basic `print` statements
3. Simple string formatting

## Learning Objectives
- Write your first Python program
- Understand basic `print` statements
- Learn how to display formatted text strings

## How to Run the Program
1. Open your terminal.
2. Navigate to the project directory.
3. Run the command: `python 01_introduction/hello_world.py`

## Code Description

**File:** [`hello_world.py`](../01_introduction/hello_world.py)

This file contains basic examples to introduce the most fundamental Python syntax and features. Below is an explanation of each part of the code:

1. **First Python program: "Hello, World!"**
   ```python
   print("Hello, World!")
   ```
   This is the classic first program in any programming language. The `print()` function is used to display text in the console.

2. **Multiple `print` statements**
   ```python
   print("Welcome to Python Programming!")
   print("This is your first step in learning Python.")
   ```
   Here, multiple `print()` calls are used to display several messages one after another.

3. **Printing different data types**
   ```python
   print(42)    # Prints an integer
   print(3.14)  # Prints a float
   print(True)  # Prints a boolean
   ```
   Python allows you to print different data types directly using the `print()` function.

4. **Basic string formatting (f-strings)**
   ```python
   name = "Learner"
   print(f"Hello, {name}!")
   ```
   This demonstrates string interpolation (`f-strings`), which allows you to insert variables inside text strings.
