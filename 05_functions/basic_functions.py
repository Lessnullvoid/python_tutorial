# Basic Functions in Python

# Simple function with no parameters
def greet():
    print("Hello, World!")

# Function with parameters
def greet_person(name):
    print(f"Hello, {name}!")

# Function with default parameter
def greet_with_time(name, time="morning"):
    print(f"Good {time}, {name}!")

# Function that returns a value
def add_numbers(a, b):
    return a + b

# Function with multiple returns
def get_user_info():
    return "John", 25, "New York"  # Returns a tuple

# Function with docstring
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Args:
        length (float): The length of the rectangle
        width (float): The width of the rectangle
    
    Returns:
        float: The area of the rectangle
    """
    return length * width

# Using the functions
print("Basic function calls:")
greet()
greet_person("Alice")
greet_with_time("Bob")
greet_with_time("Charlie", "evening")

result = add_numbers(5, 3)
print(f"\nResult of addition: {result}")

# Unpacking multiple returns
name, age, city = get_user_info()
print(f"\nUser Info - Name: {name}, Age: {age}, City: {city}")

# Using documented function
area = calculate_area(10, 20)
print(f"\nArea of rectangle: {area}")
print(f"Function documentation:\n{calculate_area.__doc__}") 