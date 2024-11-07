# Basic Problems:

## Problem 1: Count the occurrences of an item in a tuple
def count_in_tuple(my_tuple, item):
    """
    Count the number of occurrences of a specific item in a tuple.
    
    Parameters:
    my_tuple (tuple): The input tuple.
    item: The item to count.
    
    Returns:
    int: The number of occurrences of the item in the tuple.
    """
    return my_tuple.count(item)

## Problem 2: Find the index of an item in a tuple
def find_index_in_tuple(my_tuple, item):
    """
    Find the index of the first occurrence of a specific item in a tuple.
    
    Parameters:
    my_tuple (tuple): The input tuple.
    item: The item to search for.
    
    Returns:
    int: The index of the first occurrence of the item, or -1 if not found.
    """
    try:
        return my_tuple.index(item)
    except ValueError:
        return -1

# Intermediate Problems:

## Problem 1: Concatenate two tuples
def concat_tuples(t1, t2):
    """
    Concatenate two tuples into a new tuple.
    
    Parameters:
    t1 (tuple): The first tuple.
    t2 (tuple): The second tuple.
    
    Returns:
    tuple: The new tuple containing the concatenated elements.
    """
    return t1 + t2

## Problem 2: Convert a list to a tuple
def list_to_tuple(my_list):
    """
    Convert a list to a tuple.
    
    Parameters:
    my_list (list): The input list.
    
    Returns:
    tuple: The tuple created from the input list.
    """
    return tuple(my_list)

## Problem 3: Unpack a tuple into multiple variables
def unpack_tuple(my_tuple):
    """
    Unpack a tuple into multiple variables.
    
    Parameters:
    my_tuple (tuple): The input tuple.
    
    Returns:
    Tuple of variables: The unpacked variables from the tuple.
    """
    return my_tuple