"""
This is the initialization file for the package_example package.
It can be used to initialize package-level variables and imports.
"""

# Package level variables
PACKAGE_VERSION = "1.0.0"
AUTHOR = "Your Name"

# Import main functionality to make it available at package level
from .main import greet, Calculator
from .utils import format_string, validate_number

# What to export when using 'from package_example import *'
__all__ = ['greet', 'Calculator', 'format_string', 'validate_number'] 