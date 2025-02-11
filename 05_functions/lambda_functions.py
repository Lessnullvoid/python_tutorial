# Lambda Functions (Anonymous Functions)

# Basic lambda function
square = lambda x: x**2
print(f"Square of 5: {square(5)}")

# Lambda with multiple arguments
sum_numbers = lambda a, b: a + b
print(f"Sum of 3 and 4: {sum_numbers(3, 4)}")

# Using lambda with built-in functions
numbers = [1, 2, 3, 4, 5]

# map() with lambda
squares = list(map(lambda x: x**2, numbers))
print(f"\nSquares using map: {squares}")

# filter() with lambda
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers using filter: {even_numbers}")

# sorted() with lambda
points = [(1, 2), (3, 1), (0, 4), (2, 3)]
sorted_points = sorted(points, key=lambda x: x[1])  # Sort by y-coordinate
print(f"\nSorted points by y-coordinate: {sorted_points}")

# Lambda in list comprehension alternative
numbers = [1, -2, 3, -4, 5]
abs_numbers = list(map(lambda x: abs(x), numbers))
print(f"\nAbsolute values using map: {abs_numbers}")

# Lambda with conditional expression
get_status = lambda age: "adult" if age >= 18 else "minor"
print(f"\nStatus for age 20: {get_status(20)}")
print(f"Status for age 15: {get_status(15)}")

# Lambda in sorting dictionaries
people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 20}
]

sorted_by_age = sorted(people, key=lambda x: x["age"])
print("\nPeople sorted by age:")
for person in sorted_by_age:
    print(person) 