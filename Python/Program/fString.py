# Basic Problems:

## Problem 1: Format a name and age into a string
def format_name_age(name, age):
    """
    Format a name and age into a string using an f-string.
    
    Parameters:
    name (str): The person's name.
    age (int): The person's age.
    
    Returns:
    str: A formatted string with the name and age.
    """
    return f"My name is {name} and I am {age} years old."

## Problem 2: Format a number with thousands separators
def format_number(number):
    """
    Format a number with thousands separators using an f-string.
    
    Parameters:
    number (int): The number to be formatted.
    
    Returns:
    str: The number with thousands separators.
    """
    return f"{number:,}"

# Intermediate Problems:

## Problem 1: Format a date and time
from datetime import datetime

def format_datetime(dt):
    """
    Format a datetime object as a string using an f-string.
    
    Parameters:
    dt (datetime.datetime): The datetime object to be formatted.
    
    Returns:
    str: The formatted datetime string.
    """
    return f"{dt:%Y-%m-%d %H:%M:%S}"

## Problem 2: Align text within a fixed-width field
def align_text(text, width, align="left"):
    """
    Align text within a fixed-width field using an f-string.
    
    Parameters:
    text (str): The text to be aligned.
    width (int): The width of the fixed-width field.
    align (str, optional): The alignment, either "left", "right", or "center". Defaults to "left".
    
    Returns:
    str: The aligned text.
    """
    if align == "left":
        return f"{text:<{width}}"
    elif align == "right":
        return f"{text:>{width}}"
    elif align == "center":
        return f"{text:^{width}}"
    else:
        return text

## Problem 3: Format a percentage with a specific number of decimal places
def format_percentage(value, decimal_places):
    """
    Format a value as a percentage with a specified number of decimal places.
    
    Parameters:
    value (float): The value to be formatted as a percentage.
    decimal_places (int): The number of decimal places to include.
    
    Returns:
    str: The formatted percentage string.
    """
    return f"{value * 100:.{decimal_places}f}%"