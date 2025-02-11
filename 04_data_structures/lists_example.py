# Lists in Python

# Creating lists
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "orange"]
mixed = [1, "hello", 3.14, True]  # Lists can contain different types

# Accessing elements
print("List indexing:")
print(f"First element: {numbers[0]}")
print(f"Last element: {numbers[-1]}")

# Slicing lists
print("\nList slicing:")
print(f"First three elements: {numbers[0:3]}")
print(f"Every second element: {numbers[::2]}")
print(f"Reverse list: {numbers[::-1]}")

# List methods
print("\nList methods:")
fruits.append("grape")           # Add element to end
print(f"After append: {fruits}")

fruits.insert(1, "mango")       # Insert at specific position
print(f"After insert: {fruits}")

fruits.remove("banana")         # Remove specific element
print(f"After remove: {fruits}")

popped = fruits.pop()           # Remove and return last element
print(f"Popped element: {popped}")
print(f"After pop: {fruits}")

# List operations
print("\nList operations:")
combined = numbers + [6, 7, 8]  # Concatenation
print(f"Combined list: {combined}")

doubled = numbers * 2           # Repetition
print(f"Doubled list: {doubled}")

# List comprehension
squares = [x**2 for x in range(5)]
print(f"\nSquares using list comprehension: {squares}")

even_numbers = [x for x in range(10) if x % 2 == 0]
print(f"Even numbers using list comprehension: {even_numbers}")

# Sorting lists
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
print("\nSorting:")
print(f"Original list: {numbers}")
print(f"Sorted list: {sorted(numbers)}")  # Creates new sorted list
numbers.sort()                            # Sorts in place
print(f"After sort(): {numbers}")
numbers.reverse()                         # Reverses in place
print(f"After reverse(): {numbers}") 