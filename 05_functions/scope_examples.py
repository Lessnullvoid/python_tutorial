# Variable Scope in Python

# Global variable
global_var = "I am global"

def demonstrate_scope():
    # Local variable
    local_var = "I am local"
    print(f"Inside function - Local: {local_var}")
    print(f"Inside function - Global: {global_var}")

# Global keyword example
counter = 0

def increment_counter():
    global counter
    counter += 1
    print(f"Counter: {counter}")

# Nonlocal keyword example
def outer_function():
    outer_var = "Outer"
    
    def inner_function():
        nonlocal outer_var
        outer_var = "Modified by inner function"
        print(f"Inner function: {outer_var}")
    
    print(f"Before inner function: {outer_var}")
    inner_function()
    print(f"After inner function: {outer_var}")

# Demonstrating variable shadowing
x = "global"

def demonstrate_shadowing():
    x = "local"  # This creates a new local variable
    print(f"Local x: {x}")

# Using the functions
print("Demonstrating basic scope:")
demonstrate_scope()
print(f"Outside function - Global: {global_var}")
try:
    print(local_var)  # This will raise an error
except NameError as e:
    print(f"Error accessing local_var: {e}")

print("\nDemonstrating global keyword:")
increment_counter()
increment_counter()

print("\nDemonstrating nonlocal keyword:")
outer_function()

print("\nDemonstrating variable shadowing:")
print(f"Global x before function: {x}")
demonstrate_shadowing()
print(f"Global x after function: {x}")

# Scope in list comprehension (Python 3.x)
print("\nScope in list comprehension:")
i = 'global'
squares = [i for i in range(3)]
print(f"List comprehension result: {squares}")
print(f"i after list comprehension: {i}")  # i remains 'global' 