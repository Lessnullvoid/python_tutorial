# Input and Output operations in Python

# Basic input
name = input("Enter your name: ")
print(f"Hello, {name}!")

# Input with type conversion
age = int(input("Enter your age: "))
print(f"Next year, you will be {age + 1} years old")

# Multiple inputs
x, y = input("Enter two numbers separated by space: ").split()
x, y = int(x), int(y)
print(f"Sum: {x + y}")

# Formatted output
price = 49.95
quantity = 3
total = price * quantity

print("\nFormatted Output Examples:")
# Using f-strings (recommended)
print(f"Total cost: ${total:.2f}")

# Using .format()
print("Price: ${:.2f}, Quantity: {}, Total: ${:.2f}".format(price, quantity, total))

# Using % operator (older style)
print("Price: $%.2f, Quantity: %d, Total: $%.2f" % (price, quantity, total)) 