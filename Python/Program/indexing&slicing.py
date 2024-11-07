# Basic Problems:

## Problem 1: Reverse a string
def reverse_string(string):
    """
    Reverse the order of characters in a given string.
    
    Parameters:
    string (str): The input string.
    
    Returns:
    str: The reversed string.
    """
    return string[::-1]

## Problem 2: Extract the middle character(s) of a string
def get_middle_chars(string):
    """
    Extract the middle character(s) from a given string.
    
    Parameters:
    string (str): The input string.
    
    Returns:
    str: The middle character(s) of the string.
    """
    length = len(string)
    middle = length // 2
    if length % 2 == 0:
        return string[middle-1:middle+1]
    else:
        return string[middle]

# Intermediate Problems:

## Problem 1: Extract every other character from a string
def extract_every_other(string):
    """
    Extract every other character from a given string.
    
    Parameters:
    string (str): The input string.
    
    Returns:
    str: A new string containing every other character from the input.
    """
    return string[::2]

## Problem 2: Rotate a string by a given number of positions
def rotate_string(string, positions):
    """
    Rotate a string by a given number of positions to the right.
    
    Parameters:
    string (str): The input string.
    positions (int): The number of positions to rotate the string.
    
    Returns:
    str: The rotated string.
    """
    return string[-positions:] + string[:-positions]

## Problem 3: Replace a substring within a string
def replace_substring(string, old, new):
    """
    Replace a substring within a given string.
    
    Parameters:
    string (str): The input string.
    old (str): The substring to be replaced.
    new (str): The new substring to replace the old one.
    
    Returns:
    str: The modified string with the substring replaced.
    """
    return string.replace(old, new)