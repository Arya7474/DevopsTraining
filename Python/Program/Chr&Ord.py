# Basic Problems:
## Problem 1: Capitalize the first letter of a string
def capitalize_first_letter(string):
    """
    Capitalize the first letter of a given string.
    
    Parameters:
    string (str): The input string.
    
    Returns:
    str: The string with the first letter capitalized.
    """
    return string[0].upper() + string[1:]

# Problem 2: Convert a character to its ASCII value
def char_to_ascii(char):
    """
    Convert a character to its corresponding ASCII value.
    
    Parameters:
    char (str): The input character.
    
    Returns:
    int: The ASCII value of the character.
    """
    return ord(char)

# Intermediate Problems:
## Problem 1: Encode a string using ASCII values
def encode_string(string):
    """
    Encode a string by converting each character to its ASCII value.
    
    Parameters:
    string (str): The input string to be encoded.
    
    Returns:
    list: A list of ASCII values representing the input string.
    """
    return [ord(char) for char in string]

## Problem 2: Decode a list of ASCII values to a string
def decode_ascii(ascii_list):
    """
    Decode a list of ASCII values to the corresponding string.
    
    Parameters:
    ascii_list (list): A list of ASCII values.
    
    Returns:
    str: The decoded string.
    """
    return ''.join(chr(value) for value in ascii_list)

## Problem 3: Swap the case of a string
def swap_case(string):
    """
    Swap the case of each character in a given string.
    
    Parameters:
    string (str): The input string.
    
    Returns:
    str: The string with the case of each character swapped.
    """
    return ''.join(char.upper() if char.islower() else char.lower() for char in string)