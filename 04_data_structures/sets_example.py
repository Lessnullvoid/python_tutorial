# Sets in Python

# Creating sets
numbers = {1, 2, 3, 4, 5}
fruits = {"apple", "banana", "orange"}
mixed_set = {1, "hello", 3.14, True}

# Set properties
numbers_with_duplicates = {1, 2, 2, 3, 3, 4, 4, 5, 5}
print("Sets automatically remove duplicates:")
print(numbers_with_duplicates)

# Set methods
print("\nSet methods:")
fruits.add("grape")                # Add single element
print(f"After add: {fruits}")

fruits.update(["mango", "kiwi"])   # Add multiple elements
print(f"After update: {fruits}")

fruits.remove("banana")            # Remove element (raises error if not found)
print(f"After remove: {fruits}")

fruits.discard("nonexistent")      # Remove element (no error if not found)
print(f"After discard: {fruits}")

popped = fruits.pop()              # Remove and return arbitrary element
print(f"Popped element: {popped}")
print(f"After pop: {fruits}")

# Set operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("\nSet operations:")
print(f"Union: {set1 | set2}")                # Elements in either set
print(f"Intersection: {set1 & set2}")         # Elements in both sets
print(f"Difference: {set1 - set2}")           # Elements in set1 but not in set2
print(f"Symmetric difference: {set1 ^ set2}")  # Elements in either but not both

# Set comprehension
squares = {x**2 for x in range(5)}
print(f"\nSet comprehension: {squares}")

# Testing membership
print("\nMembership testing:")
print(f"Is 'apple' in fruits? {'apple' in fruits}")
print(f"Is 'banana' in fruits? {'banana' in fruits}")

# Frozen sets (immutable sets)
frozen = frozenset([1, 2, 3])
print("\nFrozen set:")
print(frozen)
try:
    frozen.add(4)  # This will raise an error
except AttributeError as e:
    print(f"Error: {e}") 