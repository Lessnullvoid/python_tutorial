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

## Concepts

### What is Python?

Python is a high-level programming language designed to be easy to read and write. It is one of the most popular languages in the world, used in web development, data science, artificial intelligence, automation, and more. Its simple syntax makes it an excellent choice for beginners.

### What is a Program?

A program is a set of instructions that tells a computer what to do, step by step. When you write a Python program, you are writing those instructions in a language the computer can understand (after Python translates them).

Think of it like a recipe: each line is a step, and the computer follows them in order from top to bottom.

### What is `print()`?

`print()` is a built-in function that displays information on the screen (the terminal/console). It is the most basic way to see the output of your program.

Syntax:

```python
print("text you want to display")
print(42)       # you can print numbers too
print(True)     # or boolean values
```

### What are f-strings?

An f-string (formatted string) lets you embed variables directly inside a text string. You prefix the string with `f` and put variable names inside curly braces `{}`.

Syntax:

```python
name = "Alice"
print(f"Hello, {name}!")  # Output: Hello, Alice!
```

This avoids clumsy string concatenation and makes your output readable.

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
