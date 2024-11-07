# Basic Problems:
## Problem 1: Shallow copy a list
def shallow_copy_list(my_list):
    """
    Create a shallow copy of a list.
    
    Parameters:
    my_list (list): The input list.
    
    Returns:
    list: A shallow copy of the input list.
    """
    return my_list.copy()

## Problem 2: Shallow copy a dictionary
def shallow_copy_dict(my_dict):
    """
    Create a shallow copy of a dictionary.
    
    Parameters:
    my_dict (dict): The input dictionary.
    
    Returns:
    dict: A shallow copy of the input dictionary.
    """
    return my_dict.copy()

# Intermediate Problems:
## Problem 1: Deep copy a nested list
import copy

def deep_copy_nested_list(my_list):
    """
    Create a deep copy of a nested list.
    
    Parameters:
    my_list (list): The input nested list.
    
    Returns:
    list: A deep copy of the input nested list.
    """
    return copy.deepcopy(my_list)

## Problem 2: Deep copy a nested dictionary
def deep_copy_nested_dict(my_dict):
    """
    Create a deep copy of a nested dictionary.
    
    Parameters:
    my_dict (dict): The input nested dictionary.
    
    Returns:
    dict: A deep copy of the input nested dictionary.
    """
    return copy.deepcopy(my_dict)