# Conditional Statements in Python

# Basic if statement
age = 18
if age >= 18:
    print("You are an adult")

# if-else statement
temperature = 25
if temperature > 30:
    print("It's hot!")
else:
    print("It's not too hot")

# if-elif-else chain
score = 85
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'
print(f"Grade: {grade}")

# Nested if statements
is_weekend = True
is_sunny = True
if is_weekend:
    if is_sunny:
        print("Let's go to the beach!")
    else:
        print("Let's watch a movie at home")
else:
    print("It's a work day")

# Conditional expressions (ternary operator)
age = 20
status = "adult" if age >= 18 else "minor"
print(f"Status: {status}")

# Using logical operators in conditions
has_ticket = True
has_id = True
if has_ticket and has_id:
    print("You can enter the venue") 