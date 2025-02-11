# Importing and Using Modules

# Standard library imports
import math
import random
from datetime import datetime
from collections import Counter

# Import our custom module
import my_module

# Using math module
print("Math module examples:")
print(f"Square root of 16: {math.sqrt(16)}")
print(f"Value of pi: {math.pi}")
print(f"Cosine of 0: {math.cos(0)}")

# Using random module
print("\nRandom module examples:")
print(f"Random number between 0 and 1: {random.random()}")
print(f"Random integer between 1 and 10: {random.randint(1, 10)}")
numbers = [1, 2, 3, 4, 5]
print(f"Random choice from list: {random.choice(numbers)}")

# Using datetime
print("\nDatetime examples:")
now = datetime.now()
print(f"Current date and time: {now}")
print(f"Formatted date: {now.strftime('%Y-%m-%d')}")

# Using collections
print("\nCollections example:")
text = "hello world hello python"
word_counts = Counter(text.split())
print(f"Word frequency: {dict(word_counts)}")

# Using our custom module
print("\nCustom module examples:")
print(f"Adding numbers: {my_module.add(10, 5)}")
print(f"Value of PI: {my_module.PI}")

# Creating a circle using our custom class
circle = my_module.Circle(radius=3)
print(f"Circle area: {circle.area():.2f}")
print(f"Circle circumference: {circle.circumference():.2f}")

# Demonstrating different import styles
from math import sqrt, pi
print("\nDirect imports:")
print(f"Square root using direct import: {sqrt(25)}")
print(f"Pi using direct import: {pi}") 