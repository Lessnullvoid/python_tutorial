# Data Structures in Python (Section 04)

This section covers Python's built-in data structures and their operations.

## Code Description

- [`lists_example.py`](../04_data_structures/lists_example.py): Shows how to create, access, and manipulate lists in Python.
- [`tuples_example.py`](../04_data_structures/tuples_example.py): Explains how to use tuples, highlighting their immutability and practical use cases.
- [`dictionaries_example.py`](../04_data_structures/dictionaries_example.py): Presents dictionary usage, including safe access and common methods.
- [`sets_example.py`](../04_data_structures/sets_example.py): Demonstrates how to work with sets and perform operations like union and intersection.
- [`list_comprehension.py`](../04_data_structures/list_comprehension.py): Contains advanced examples of list and dictionary comprehensions for efficient data manipulation.

## Learning Objectives
1. Understand and effectively use Python's built-in data structures.
2. Perform operations with lists, tuples, dictionaries, and sets.
3. Implement list and dictionary comprehensions for data manipulation.
4. Apply these structures in practical programming scenarios.

## Concepts

### What is a Data Structure?

A data structure is a way of organizing and storing multiple pieces of data so you can access and modify them efficiently. Instead of creating separate variables for 100 items, you put them in a single structure.

### What is a List?

A list is an ordered, mutable collection of items. "Ordered" means items keep their position. "Mutable" means you can add, remove, or change items after creating the list.

```python
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")  # add to the end
fruits[0]                 # access by position: "apple"
```

Use lists when you have a sequence of items that might change.

### What is a Tuple?

A tuple is like a list, but **immutable** -- once created, you cannot change its contents. This makes tuples useful for data that should not be accidentally modified.

```python
coordinates = (10, 20)
name, age = ("Alice", 25)  # unpacking
```

Use tuples for fixed collections like coordinates, RGB colors, or returning multiple values from a function.

### What is a Dictionary?

A dictionary stores data as **key-value pairs**. Instead of accessing items by position (index), you access them by a unique key name.

```python
person = {"name": "Alice", "age": 25, "city": "Berlin"}
person["name"]  # "Alice"
```

Think of it like a real dictionary: you look up a word (key) to find its definition (value). Use dictionaries when you want to label and quickly look up data.

### What is a Set?

A set is an unordered collection of **unique** items. It automatically removes duplicates and supports mathematical operations like union and intersection.

```python
colors = {"red", "green", "blue", "red"}  # becomes {"red", "green", "blue"}
```

Use sets when you need to eliminate duplicates or perform membership tests quickly.

### What is a List Comprehension?

A list comprehension is a concise way to create a new list by applying an expression to each item in an existing sequence, all in a single line:

```python
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
```

It replaces the pattern of: create empty list, loop, append -- making your code shorter and more readable.

## Detailed Code Description

### lists_example.py
This file shows how to work with **lists in Python**, including creation, indexing, methods, and list comprehensions.

**Code examples:**
```python
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "orange"]
```
```python
squares = [x**2 for x in range(5)]
```

### tuples_example.py
This file explains how to use **tuples in Python**, highlighting their immutability and practical applications.

**Code examples:**
```python
coordinates = (10, 20)
name, age, city = ("John", 25, "New York")
```

### dictionaries_example.py
This file shows how to create and manipulate **dictionaries in Python**, including safe key access and common methods.

**Code examples:**
```python
person = {"name": "John", "age": 30}
print(person["name"])
```
```python
squares = {x: x**2 for x in range(5)}
```

### sets_example.py
This file explains how to work with **sets in Python**, including operations like union, intersection, and difference.

**Code examples:**
```python
numbers = {1, 2, 3, 4, 5}
union = set1 | set2
```

### list_comprehension.py
This file contains advanced examples of **list and dictionary comprehensions**, showing how to create complex data structures concisely.

**Code examples:**
```python
squares = [x**2 for x in range(5)]
flattened = [num for row in matrix for num in row]
```

## How to Run the Programs

1. Make sure Python is installed on your machine.
2. Navigate to the project directory in your terminal.
3. Use the command `python 04_data_structures/<filename>.py` to run the desired program, replacing `<filename>` with the specific file name (for example, `python 04_data_structures/lists_example.py`).
