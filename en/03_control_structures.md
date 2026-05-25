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
