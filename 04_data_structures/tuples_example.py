# Tuples in Python

# Creating tuples
coordinates = (10, 20)
person = ("John", 25, "New York")
single_element = (42,)  # Note the comma for single-element tuple

# Accessing elements
print("Tuple indexing:")
print(f"X coordinate: {coordinates[0]}")
print(f"Y coordinate: {coordinates[1]}")

# Tuple unpacking
print("\nTuple unpacking:")
name, age, city = person
print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")

# Multiple assignment with tuples
x, y = coordinates
print(f"\nUnpacked coordinates: x={x}, y={y}")

# Tuple methods
numbers = (1, 2, 3, 2, 4, 2, 5)
print("\nTuple methods:")
print(f"Count of 2: {numbers.count(2)}")
print(f"Index of 4: {numbers.index(4)}")

# Immutability demonstration
try:
    coordinates[0] = 100  # This will raise an error
except TypeError as e:
    print("\nTuples are immutable:")
    print(f"Error: {e}")

# Nested tuples
matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print("\nNested tuples:")
for row in matrix:
    print(row)

# Converting between lists and tuples
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print("\nConversion:")
print(f"List to tuple: {my_tuple}")
print(f"Tuple to list: {list(my_tuple)}")

# Using tuples as dictionary keys (unlike lists)
locations = {
    (0, 0): "Origin",
    (1, 1): "Point A",
    (-1, -1): "Point B"
}
print("\nTuples as dictionary keys:")
print(locations[(0, 0)]) 