# Basic Problems:

## Problem 1: Count the occurrences of a character in a string
def count_char(string, char):
    """
    Count the number of occurrences of a given character in a string.
    
    Parameters:
    string (str): The input string.
    char (str): The character to count.
    
    Returns:
    int: The number of occurrences of the character in the string.
    """
    return string.count(char)

## Problem 2: Check if a string starts or ends with a specific substring
def check_substring(string, substr, start_or_end):
    """
    Check if a string starts or ends with a specific substring.
    
    Parameters:
    string (str): The input string.
    substr (str): The substring to check.
    start_or_end (str): Either "start" or "end" to indicate the check.
    
    Returns:
    bool: True if the string starts/ends with the substring, False otherwise.
    """
    if start_or_end == "start":
        return string.startswith(substr)
    elif start_or_end == "end":
        return string.endswith(substr)
    else:
        return False

# Intermediate Problems:

## Problem 1: Remove leading and trailing whitespace from a string
def trim_whitespace(string):
    """
    Remove leading and trailing whitespace from a given string.
    
    Parameters:
    string (str): The input string.
    
    Returns:
    str: The string with leading and trailing whitespace removed.
    """
    return string.strip()

## Problem 2: Convert a string to title case
def to_title_case(string):
    """
    Convert a string to title case (first letter of each word capitalized).
    
    Parameters:
    string (str): The input string.
    
    Returns:
    str: The string in title case.
    """
    return string.title()

## Problem 3: Split a string into a list based on a delimiter
def split_string(string, delimiter):
    """
    Split a string into a list based on a given delimiter.
    
    Parameters:
    string (str): The input string.
    delimiter (str): The character or sequence to use as the delimiter.
    
    Returns:
    list: A list of substrings from the input string.
    """
    return string.split(delimiter)