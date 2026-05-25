# File Handling in Python (Section 07)

This section covers file operations, including text, CSV, JSON, and exception handling.

## Code Description

- [`file_operations.py`](../07_file_handling/file_operations.py): Shows how to perform basic read, write, and append operations on text files.
- [`csv_operations.py`](../07_file_handling/csv_operations.py): Demonstrates how to handle CSV files using the `csv` module.
- [`json_operations.py`](../07_file_handling/json_operations.py): Illustrates how to work with JSON data, including serialization and deserialization.
- [`exception_handling.py`](../07_file_handling/exception_handling.py): Provides examples of exception handling to ensure safe file operations.

## Learning Objectives

You will learn how to:
1. Open and close files in Python.
2. Read and write text, CSV, and JSON files.
3. Implement error handling to ensure robust operations.

## Concepts

### What is a File?

A file is a named location on your disk that stores data permanently. Unlike variables (which disappear when your program ends), files persist after the program closes. Programs read files to get data and write files to save results.

### What is Reading and Writing?

- **Reading**: opening a file and loading its contents into your program.
- **Writing**: creating or overwriting a file with new content.
- **Appending**: adding content to the end of an existing file without erasing what was there.

Python uses the `open()` function with mode flags:

```python
open("file.txt", "r")   # read
open("file.txt", "w")   # write (overwrites!)
open("file.txt", "a")   # append
```

The `with` statement ensures the file is properly closed when you're done:

```python
with open("file.txt", "r") as f:
    content = f.read()
```

### What is CSV?

CSV (Comma-Separated Values) is a simple file format for tabular data (like a spreadsheet). Each line is a row, and values in each row are separated by commas.

```
name,age,city
Alice,25,Berlin
Bob,30,Madrid
```

Python's built-in `csv` module makes it easy to read and write these files.

### What is JSON?

JSON (JavaScript Object Notation) is a lightweight format for storing structured data. It looks like Python dictionaries and lists, making it intuitive to work with.

```json
{"name": "Alice", "age": 25, "hobbies": ["reading", "coding"]}
```

Python's `json` module converts between Python objects and JSON strings (serialization/deserialization).

### What is an Exception?

An exception is an error that occurs while your program is running (not a typo in your code, but something unexpected like a missing file or invalid input). Instead of crashing, you can "catch" exceptions and handle them gracefully:

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

This is essential for file operations because files might not exist, might be locked, or might contain unexpected data.

## Detailed Code Description

### file_operations.py
This file shows how to perform **basic file operations in Python**.

**Code examples:**
```python
with open("sample.txt", "w") as file:
    file.write("Hello, this is line 1\n")
```
```python
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)
```

### csv_operations.py
This file demonstrates how to handle **CSV files in Python** using the `csv` module.

**Code examples:**
```python
with open('people.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(sample_data)
```
```python
with open('people.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

### json_operations.py
This file illustrates how to work with **JSON files in Python**.

**Code examples:**
```python
with open('data.json', 'w') as file:
    json.dump(sample_data, file, indent=4)
```
```python
with open('data.json', 'r') as file:
    data = json.load(file)
    print(data)
```

### exception_handling.py
This file shows how to implement **exception handling for file operations**.

**Code examples:**
```python
try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: File does not exist")
```
```python
try:
    number = int("abc")
except ValueError:
    print("Error: Invalid number format")
```

## How to Run the Programs

1. Make sure Python is installed on your machine.
2. Navigate to the project directory in your terminal.
3. Run the desired script using the command:
   ```bash
   python 07_file_handling/<script_name>.py
   ```
   Replace `<script_name>` with the name of the file you want to run (for example, `file_operations`).
