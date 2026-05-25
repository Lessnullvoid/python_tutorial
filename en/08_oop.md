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

## Concepts

### What is Object-Oriented Programming?

Object-Oriented Programming (OOP) is a way of organizing code around "objects" -- things that combine data and behavior together. Instead of having separate variables and functions scattered around, you group related data and the functions that operate on that data into a single unit.

Think of it like modeling the real world: a "Car" object has data (color, speed, fuel level) and behaviors (accelerate, brake, refuel).

### What is a Class?

A class is a blueprint or template for creating objects. It defines what data (attributes) and behaviors (methods) the objects will have.

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name      # attribute
        self.breed = breed    # attribute

    def bark(self):           # method
        return "Woof!"
```

### What is an Object?

An object is a specific instance created from a class. You can create many objects from the same class, each with different data.

```python
my_dog = Dog("Rex", "Labrador")   # object 1
your_dog = Dog("Luna", "Poodle")  # object 2
```

### What is Encapsulation?

Encapsulation means hiding a class's internal data and only exposing what's necessary through methods. This protects data from being changed accidentally.

- `_name` -- convention for "protected" (should not be accessed directly from outside)
- `__name` -- "private" (Python makes it harder to access from outside)

Think of it like a bank account: you can't directly change the balance; you must use deposit() or withdraw() which enforce rules.

### What is Inheritance?

Inheritance lets a new class (child) reuse the code of an existing class (parent). The child gets all the parent's attributes and methods, and can add or override them.

```python
class Animal:         # parent
    def speak(self):
        pass

class Cat(Animal):    # child inherits from Animal
    def speak(self):
        return "Meow!"
```

This avoids duplicating code when multiple classes share common behavior.

### What is Polymorphism?

Polymorphism means "many forms" -- different classes can have methods with the same name that behave differently. This lets you write code that works with any object that has the expected method, regardless of its specific class.

```python
for animal in [Cat(), Dog(), Duck()]:
    print(animal.speak())  # each responds differently
```

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
