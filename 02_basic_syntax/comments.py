# This is a single-line comment

"""
This is a multi-line comment (docstring)
It can span multiple lines
And is often used for documentation
"""

# Variables with comments
name = "John"  # User's name
age = 25       # User's age

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

# Example of commenting code logic
# Check if person is eligible to vote
age = 18
if age >= 18:    # Voting age check
    print("Eligible to vote")
else:
    print("Not eligible to vote")

# TODO: This is a TODO comment, often used to mark future tasks
# FIXME: This is a FIXME comment, used to mark bugs that need fixing
# NOTE: This is a NOTE comment, used for important notes about the code 