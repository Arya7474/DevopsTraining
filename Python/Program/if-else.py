# Basic Problems:

## Problem 1: Determine the largest of three numbers
def find_largest(a, b, c):
    """
    Determine the largest of three numbers.
    
    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.
    c (int or float): The third number.
    
    Returns:
    int or float: The largest of the three numbers.
    """
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

## Problem 2: Check if a number is positive, negative, or zero
def check_number(num):
    """
    Determine whether a number is positive, negative, or zero.
    
    Parameters:
    num (int or float): The number to be checked.
    
    Returns:
    str: "Positive" if the number is positive, "Negative" if the number is negative, "Zero" if the number is zero.
    """
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

# Intermediate Problems:

## Problem 1: Determine the grade based on a score
def get_grade(score):
    """
    Determine the grade based on a numerical score.
    
    Parameters:
    score (int): The numerical score.
    
    Returns:
    str: The corresponding letter grade.
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

## Problem 2: Check if a year is a leap year
def is_leap_year(year):
    """
    Determine if a year is a leap year.
    
    Parameters:
    year (int): The year to be checked.
    
    Returns:
    bool: True if the year is a leap year, False otherwise.
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

## Problem 3: Implement a simple calculator
def calculator(a, b, operator):
    """
    Implement a simple calculator with basic arithmetic operations.
    
    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.
    operator (str): The arithmetic operation to perform (+, -, *, /).
    
    Returns:
    int or float: The result of the arithmetic operation.
    """
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operator"