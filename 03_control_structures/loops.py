# Loops in Python

# For Loops
print("Basic for loop with range:")
for i in range(5):
    print(i)

# For loop with start, stop, step
print("\nFor loop with start, stop, step:")
for i in range(2, 10, 2):  # Start at 2, stop before 10, step by 2
    print(i)

# For loop with list
print("\nIterating through a list:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# For loop with enumerate
print("\nUsing enumerate:")
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# While Loops
print("\nBasic while loop:")
count = 0
while count < 5:
    print(count)
    count += 1

# While loop with condition
print("\nWhile loop with condition:")
number = 10
while number > 0:
    print(number)
    number -= 2

# Nested loops
print("\nNested loops:")
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")

# Loop with dictionary
print("\nLooping through dictionary:")
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

for key in person:
    print(f"{key}: {person[key]}")

# Alternative dictionary iteration
for key, value in person.items():
    print(f"{key}: {value}") 