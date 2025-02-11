# Loop Control Statements in Python

# Break statement
print("Break example:")
for i in range(1, 6):
    if i == 4:
        break
    print(i)
print("Loop ended")

# Continue statement
print("\nContinue example:")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# While loop with break
print("\nWhile loop with break:")
counter = 0
while True:
    print(counter)
    counter += 1
    if counter >= 5:
        break

# Nested loops with break
print("\nNested loops with break:")
for i in range(3):
    for j in range(3):
        if j == 2:
            break
        print(f"i: {i}, j: {j}")

# Using else with loops
print("\nLoop with else:")
for i in range(5):
    if i == 10:  # This condition will never be True
        break
    print(i)
else:
    print("Loop completed without break")

# Example: Finding a number in a list
print("\nFinding number in list:")
numbers = [1, 3, 5, 7, 9, 11, 13]
search_for = 7

for num in numbers:
    if num == search_for:
        print(f"Found {search_for}!")
        break
else:
    print(f"{search_for} not found in the list")

# Pass statement
print("\nPass statement example:")
for i in range(3):
    if i == 1:
        pass  # Do nothing
    else:
        print(i) 