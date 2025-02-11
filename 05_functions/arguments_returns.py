# Function Arguments and Return Values

# Positional arguments
def print_info(name, age, city):
    print(f"Name: {name}, Age: {age}, City: {city}")

# Keyword arguments
def calculate_payment(principal, rate=5, years=1):
    return principal * (1 + rate/100) ** years

# Variable number of positional arguments
def sum_all(*args):
    """Sum any number of positional arguments"""
    return sum(args)

# Variable number of keyword arguments
def print_kwargs(**kwargs):
    """Print all keyword arguments"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Combining different types of arguments
def mixed_arguments(a, b, *args, option=True, **kwargs):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"args: {args}")
    print(f"option: {option}")
    print(f"kwargs: {kwargs}")

# Multiple return values
def get_statistics(numbers):
    """Calculate basic statistics for a list of numbers"""
    return min(numbers), max(numbers), sum(numbers)/len(numbers)

# Using the functions
print("Positional arguments:")
print_info("John", 30, "New York")

print("\nKeyword arguments:")
payment = calculate_payment(principal=1000, rate=7, years=2)
print(f"Payment: {payment:.2f}")

print("\nVariable positional arguments:")
result = sum_all(1, 2, 3, 4, 5)
print(f"Sum: {result}")

print("\nVariable keyword arguments:")
print_kwargs(name="Alice", age=25, city="London", job="Developer")

print("\nMixed arguments:")
mixed_arguments(1, 2, 3, 4, 5, option=False, x=10, y=20)

print("\nMultiple return values:")
numbers = [1, 2, 3, 4, 5]
minimum, maximum, average = get_statistics(numbers)
print(f"Min: {minimum}, Max: {maximum}, Average: {average}") 