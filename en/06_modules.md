# Modules and Packages in Python (Section 06)

This section covers module creation, importing, and package organization in Python.

## Code Description

- [`my_module.py`](../06_modules/my_module.py): Demonstrates how to create a module with basic math functions and a `Circle` class.
- [`using_modules.py`](../06_modules/using_modules.py): Shows how to import and use standard and custom modules.
- [`package_example/`](../06_modules/package_example/): A sample package containing:
  - [`__init__.py`](../06_modules/package_example/__init__.py): Initializes the package, making main functions and classes accessible at the package level.
  - [`main.py`](../06_modules/package_example/main.py): Defines the package's main functionality, including the `Calculator` class.
  - [`utils.py`](../06_modules/package_example/utils.py): Provides utility functions for string formatting and number validation.

## Learning Objectives
1. Create and use modules in Python.
2. Import standard and custom modules.
3. Organize Python files into packages.
4. Use third-party packages via `pip`.
5. Create and test your own Python package.

## Detailed Code Description

### my_module.py
This file shows how to create a **custom Python module** with functions, constants, and classes.

**Code examples:**
```python
def add(a, b):
    return a + b

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return PI * self.radius ** 2
```

### using_modules.py
This file shows how to **import and use standard and custom modules** in Python.

**Code examples:**
```python
import math
print(math.sqrt(16))  # Result: 4.0

import my_module
print(my_module.add(10, 5))
```

### package_example/__init__.py
This file initializes the package and **makes main functions and classes accessible** at the package level.

**Key content:**
```python
PACKAGE_VERSION = "1.0.0"
AUTHOR = "Your Name"
from .main import greet, Calculator
from .utils import format_string
```

### package_example/main.py
This file defines the **package's main functionality**.

**Code examples:**
```python
def greet(name):
    return f"Hello, {name}!"

class Calculator:
    @staticmethod
    def add(a, b):
        return a + b
```

### package_example/utils.py
This file provides **utility functions** for string formatting and number validation.

**Code examples:**
```python
def format_string(text, uppercase=False):
    return text.upper() if uppercase else text.lower()

def validate_number(number):
    try:
        float(number)
        return True
    except (TypeError, ValueError):
        return False
```

## How to Run the Programs

1. Make sure Python is installed on your machine.
2. Navigate to the project directory.
3. Use the command line to run a specific program. For example:
   ```bash
   python 06_modules/using_modules.py
   ```
