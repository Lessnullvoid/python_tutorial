# Control Structures in Python (Section 03)

This section covers flow control mechanisms in Python, including conditionals and loops.

## Code Description

- [`conditionals.py`](../03_control_structures/conditionals.py): Illustrates decision-making in Python using conditional statements.
- [`loops.py`](../03_control_structures/loops.py): Demonstrates various loop constructs in Python.
- [`loop_control.py`](../03_control_structures/loop_control.py): Shows how to control loop execution with statements like `break` and `continue`.

## Learning Objectives
- Understand the different types of loops in Python and when to use them.
- Learn to control loop execution with `break`, `continue`, and `pass` statements.
- Gain proficiency in using conditional statements to make decisions in code.

## Concepts

### What is Flow Control?

By default, Python runs your code line by line from top to bottom. Flow control lets you change this: you can skip lines, repeat lines, or choose between different paths. Conditionals and loops are the two main tools for flow control.

### What is a Conditional?

A conditional lets your program make decisions. Instead of running every line, the program checks a condition and chooses which path to follow.

Think of it like a fork in the road: "If it's raining, take an umbrella. Otherwise, wear sunglasses."

In Python, you write conditionals with `if`, `elif`, and `else`:

```python
if condition:
    # runs only when condition is True
elif other_condition:
    # runs if the first was False but this one is True
else:
    # runs when nothing above was True
```

The indented block under each keyword is what runs for that branch. Only ONE branch executes.

### What is a Loop?

A loop repeats a block of code multiple times. Instead of writing the same instruction 100 times, you write it once inside a loop.

Python has two types of loops:

- **for loop** -- repeats once for each item in a sequence (a list, a range of numbers, etc.)
- **while loop** -- repeats as long as a condition remains True

```python
for item in sequence:
    # do something with item

while condition:
    # do something until condition becomes False
```

A `for` loop is best when you know how many times to repeat. A `while` loop is best when you repeat until something changes.

### What is Loop Control?

Sometimes you need to alter a loop's behavior mid-execution:

- `break` -- stop the loop entirely and continue with the code after it
- `continue` -- skip the rest of the current iteration and jump to the next one
- `pass` -- do nothing (a placeholder when syntax requires a body but you have nothing to do yet)

## Detailed Code Description

### conditionals.py
This file shows how to use **conditional structures in Python**, such as `if`, `elif`, and `else`, to make decisions based on different conditions.

**Code examples:**
```python
age = 18
if age >= 18:
    print("You are an adult")
```
```python
temperature = 25
if temperature > 30:
    print("It's hot!")
else:
    print("It's not too hot")
```

### loops.py
This file presents different types of **loops in Python**, such as `for` and `while`, to repeat actions.

**Code examples:**
```python
for i in range(5):
    print(i)
```
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```
```python
count = 0
while count < 5:
    print(count)
    count += 1
```

### loop_control.py
This file illustrates how to control **loop execution in Python** using `break`, `continue`, and `pass` statements.

**Code examples:**
```python
for i in range(1, 6):
    if i == 4:
        break
    print(i)
```
```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

## How to Run the Programs

1. Make sure Python is installed on your machine.
2. Open a terminal or command prompt.
3. Navigate to the project directory.
4. Run the desired program using the command:
   ```bash
   python 03_control_structures/<filename>.py
   ```
   Replace `<filename>` with `loops`, `loop_control`, or `conditionals` as needed.
