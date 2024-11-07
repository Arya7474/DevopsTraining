# Basic Problems:

## Problem 1: Create a function to calculate the area of a rectangle
def rectangle_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Parameters:
    length (int or float): The length of the rectangle.
    width (int or float): The width of the rectangle.
    
    Returns:
    int or float: The area of the rectangle.
    """
    return length * width

## Problem 2: Create a function to check if a number is prime
def is_prime(num):
    """
    Determine if a number is prime.
    
    Parameters:
    num (int): The number to be checked.
    
    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Intermediate Problems:

## Problem 1: Create a function to calculate the nth Fibonacci number
def fibonacci(n):
    """
    Calculate the nth Fibonacci number.
    
    Parameters:
    n (int): The position of the Fibonacci number to be calculated.
    
    Returns:
    int: The nth Fibonacci number.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

## Problem 2: Create a function to reverse a string
def reverse_string(string):
    """
    Reverse a given string.
    
    Parameters:
    string (str): The input string to be reversed.
    
    Returns:
    str: The reversed string.
    """
    return string[::-1]

## Problem 3: Create a function to find the maximum number in a list
def find_max(num_list):
    """
    Find the maximum number in a list.
    
    Parameters:
    num_list (list): The list of numbers.
    
    Returns:
    int or float: The maximum number in the list.
    """
    return max(num_list)