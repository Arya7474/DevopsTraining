# Basic Problems:

## Problem 1: Print the elements of a list
def print_list(my_list):
    """
    Print each element of a list.
    
    Parameters:
    my_list (list): The input list.
    """
    for item in my_list:
        print(item)

## Problem 2: Calculate the sum of elements in a list
def sum_of_list(my_list):
    """
    Calculate the sum of all elements in a list.
    
    Parameters:
    my_list (list): The input list.
    
    Returns:
    int or float: The sum of the elements in the list.
    """
    total = 0
    for num in my_list:
        total += num
    return total

# Intermediate Problems:

## Problem 1: Iterate over a dictionary and print key-value pairs
def print_dict(my_dict):
    """
    Iterate over a dictionary and print each key-value pair.
    
    Parameters:
    my_dict (dict): The input dictionary.
    """
    for key, value in my_dict.items():
        print(f"{key}: {value}")

## Problem 2: Create a histogram from a list of numbers
def create_histogram(num_list):
    """
    Create a histogram from a list of numbers.
    
    Parameters:
    num_list (list): The input list of numbers.
    """
    histogram = {}
    for num in num_list:
        if num in histogram:
            histogram[num] += 1
        else:
            histogram[num] = 1
    
    for key, value in histogram.items():
        print(f"{key}: {"#" * value}")

## Problem 3: Find the most common element in a list
def most_common_element(my_list):
    """
    Find the most common element in a list.
    
    Parameters:
    my_list (list): The input list.
    
    Returns:
    Any: The most common element in the list.
    """
    element_counts = {}
    for item in my_list:
        if item in element_counts:
            element_counts[item] += 1
        else:
            element_counts[item] = 1
    
    return max(element_counts, key=element_counts.get)