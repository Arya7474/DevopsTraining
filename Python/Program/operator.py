# Basic Problems:

## Problem 1: Perform basic arithmetic operations
def arithmetic_operations(a, b):
    """
    Perform basic arithmetic operations on two numbers.
    
    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.
    
    Returns:
    Tuple[int or float, int or float, int or float, int or float, int or float]: 
    The results of addition, subtraction, multiplication, division, and modulo operations.
    """
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b
    modulo = a % b
    return addition, subtraction, multiplication, division, modulo

## Problem 2: Check if a number is even or odd
def is_even_odd(num):
    """
    Check if a number is even or odd.
    
    Parameters:
    num (int): The number to be checked.
    
    Returns:
    str: "Even" if the number is even, "Odd" if the number is odd.
    """
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Intermediate Problems:

## Problem 1: Check if a number is within a certain range
def is_in_range(num, min_value, max_value):
    """
    Check if a number is within a specified range (inclusive).
    
    Parameters:
    num (int or float): The number to be checked.
    min_value (int or float): The minimum value of the range.
    max_value (int or float): The maximum value of the range.
    
    Returns:
    bool: True if the number is within the range, False otherwise.
    """
    return min_value <= num <= max_value

## Problem 2: Perform chained comparisons
def chained_comparison(a, b, c):
    """
    Perform chained comparisons on three numbers.
    
    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.
    c (int or float): The third number.
    
    Returns:
    bool: True if the chained comparison is true, False otherwise.
    """
    return a < b < c