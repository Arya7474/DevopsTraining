# Basic Problems:

## Problem 1: Create a function with required parameters
def greet(name, greeting="Hello"):
    """
    Greet a person with a customizable greeting.
    
    Parameters:
    name (str): The name of the person to be greeted.
    greeting (str, optional): The greeting to be used. Defaults to "Hello".
    
    Returns:
    str: The greeting message.
    """
    return f"{greeting}, {name}!"

## Problem 2: Create a function with default parameter values
def calculate_area(length, width=1):
    """
    Calculate the area of a rectangle.
    
    Parameters:
    length (int or float): The length of the rectangle.
    width (int or float, optional): The width of the rectangle. Defaults to 1.
    
    Returns:
    int or float: The area of the rectangle.
    """
    return length * width

# Intermediate Problems:

## Problem 1: Create a function with a variable number of arguments
def sum_numbers(*args):
    """
    Calculate the sum of a variable number of arguments.
    
    Parameters:
    *args: A variable number of numeric arguments.
    
    Returns:
    int or float: The sum of the arguments.
    """
    return sum(args)

## Problem 2: Create a function with keyword arguments
def print_student_info(name, age, **kwargs):
    """
    Print student information with additional keyword arguments.
    
    Parameters:
    name (str): The name of the student.
    age (int): The age of the student.
    **kwargs: Additional keyword arguments (e.g., grade, gpa, email).
    """
    print(f"Name: {name}, Age: {age}")
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")