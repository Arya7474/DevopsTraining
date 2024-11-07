# Basic Problems:

## Problem 1: Handle a ZeroDivisionError
def safe_divide(a, b):
    """
    Safely divide two numbers, handling ZeroDivisionError.
    
    Parameters:
    a (int or float): The dividend.
    b (int or float): The divisor.
    
    Returns:
    float: The result of the division, or None if the divisor is 0.
    """
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Division by zero.")
        return None

## Problem 2: Handle a ValueError
def convert_to_int(value):
    """
    Convert a value to an integer, handling ValueError.
    
    Parameters:
    value (str): The value to be converted.
    
    Returns:
    int: The converted integer value, or None if the conversion fails.
    """
    try:
        return int(value)
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")
        return None

# Intermediate Problems:

## Problem 1: Handle multiple exceptions
def divide_and_square(a, b):
    """
    Divide two numbers, then square the result, handling ZeroDivisionError and TypeError.
    
    Parameters:
    a (int or float): The dividend.
    b (int or float): The divisor.
    
    Returns:
    float: The square of the division result, or None if an exception occurs.
    """
    try:
        result = a / b
        return result ** 2
    except ZeroDivisionError:
        print("Error: Division by zero.")
        return None
    except TypeError:
        print("Error: Invalid input types. Please provide numeric values.")
        return None

