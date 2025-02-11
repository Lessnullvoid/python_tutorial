"""
Utility functions for the package
"""

def format_string(text, uppercase=False):
    """Format a string based on parameters"""
    if uppercase:
        return text.upper()
    return text.lower()

def validate_number(number):
    """Validate if a value is a number"""
    try:
        float(number)
        return True
    except (TypeError, ValueError):
        return False

def _internal_helper():
    """Internal helper function not meant to be used directly"""
    pass 