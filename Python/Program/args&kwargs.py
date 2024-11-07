# Basic Problems:
## Problem 1: Create a function that sums up a variable number of arguments
def sum_numbers(*args):
    """
    Calculate the sum of a variable number of numeric arguments.
    
    Parameters:
    *args: A variable number of numeric arguments.
    
    Returns:
    int or float: The sum of the arguments.
    """
    return sum(args)

## Problem 2: Create a function that prints key-value pairs from a variable number of keyword arguments
def print_kwargs(**kwargs):
    """
    Print the key-value pairs of a variable number of keyword arguments.
    
    Parameters:
    **kwargs: A variable number of keyword arguments.
    """
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Intermediate Problems:
## Problem 1: Create a function that concatenates strings from a variable number of arguments
def concat_strings(*args):
    """
    Concatenate a variable number of string arguments.
    
    Parameters:
    *args: A variable number of string arguments.
    
    Returns:
    str: The concatenated string.
    """
    return "".join(args)

## Problem 2: Create a function that can accept both positional and keyword arguments
def calculate_stats(name, *args, **kwargs):
    """
    Calculate various statistics based on a variable number of numeric arguments.
    
    Parameters:
    name (str): The name associated with the statistics.
    *args: A variable number of numeric arguments.
    **kwargs: A variable number of keyword arguments (e.g., "max", "min", "mean").
    
    Returns:
    dict: A dictionary containing the requested statistics.
    """
    stats = {
        "name": name,
        "sum": sum(args),
        "count": len(args),
        "min": min(args),
        "max": max(args),
        "mean": sum(args) / len(args)
    }
    
    for key, func in kwargs.items():
        stats[key] = func(args)
    
    return stats