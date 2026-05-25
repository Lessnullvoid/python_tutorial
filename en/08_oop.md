# Object-Oriented Programming in Python (Section 08)

This section covers object-oriented programming (OOP) concepts and their implementation in Python.

## Code Description

- [`classes.py`](../08_oop/classes.py): Introduces the creation and use of classes and objects, including methods and attributes.
- [`encapsulation.py`](../08_oop/encapsulation.py): Shows how to implement encapsulation to protect a class's internal data.
- [`inheritance.py`](../08_oop/inheritance.py): Demonstrates how inheritance works, including single and multiple inheritance.
- [`polymorphism.py`](../08_oop/polymorphism.py): Illustrates polymorphism through abstract classes, method overriding, and operator overloading.

## Section Contents

In this section, we will explore the fundamental concepts of object-oriented programming:
1. Classes and Objects
2. Encapsulation
3. Inheritance
4. Polymorphism

## Detailed Code Description

### classes.py
This file introduces the creation and use of **classes and objects in Python**.

**Code examples:**
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."
```
```python
@staticmethod
def is_adult(age):
    return age >= 18
```

### encapsulation.py
This file shows how to implement **encapsulation in Python**, protecting a class's internal data.

**Code examples:**
```python
self._account_holder = account_holder  # Protected attribute
self.__balance = initial_balance       # Private attribute
```
```python
def deposit(self, amount):
    self.__balance += amount
```

### inheritance.py
This file demonstrates how **inheritance works in Python**, including single and multiple inheritance.

**Code examples:**
```python
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed

    def make_sound(self):
        return "Woof!"
```

### polymorphism.py
This file illustrates **polymorphism in Python** through abstract classes and operator overloading.

**Code examples:**
```python
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
```
```python
def __add__(self, other):
    return Vector(self.x + other.x, self.y + other.y)
```

## How to Run the Programs

1. Make sure Python is installed on your machine.
2. Navigate to the project directory.
3. Use the command line to run a specific program. For example:
   ```bash
   python 08_oop/classes.py
   ```
