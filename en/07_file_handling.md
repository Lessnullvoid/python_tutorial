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
