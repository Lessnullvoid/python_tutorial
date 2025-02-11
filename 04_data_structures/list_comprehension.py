# List Comprehension Examples

# Basic list comprehension
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(f"Squares: {squares}")

# List comprehension with condition
even_squares = [x**2 for x in numbers if x % 2 == 0]
print(f"\nEven squares: {even_squares}")

# Nested list comprehension
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

flattened = [num for row in matrix for num in row]
print(f"\nFlattened matrix: {flattened}")

# List comprehension with strings
words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words]
print(f"\nUppercase words: {upper_words}")

# Conditional list comprehension with else
numbers = [-4, -2, 0, 2, 4]
absolute = [x if x >= 0 else -x for x in numbers]
print(f"\nAbsolute values: {absolute}")

# Creating a matrix using list comprehension
matrix = [[i + j for j in range(3)] for i in range(0, 9, 3)]
print("\nMatrix created with list comprehension:")
for row in matrix:
    print(row)

# List comprehension with zip
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
people = [f"{name} is {age} years old" for name, age in zip(names, ages)]
print("\nPeople information:")
for person in people:
    print(person)

# Set comprehension
numbers = [1, 2, 2, 3, 3, 4, 4, 5, 5]
unique_squares = {x**2 for x in numbers}
print(f"\nUnique squares (set): {unique_squares}")

# Dictionary comprehension
word_lengths = {word: len(word) for word in words}
print(f"\nWord lengths: {word_lengths}")

# Multiple if conditions
numbers = range(1, 51)
special_numbers = [x for x in numbers if x % 3 == 0 if x % 5 == 0]
print(f"\nNumbers divisible by both 3 and 5: {special_numbers}") 