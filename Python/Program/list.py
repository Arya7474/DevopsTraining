# Basic Problems:

## Problem 1: Append an item to a list
def append_to_list(my_list, item):
    """
    Append an item to the end of a list.
    
    Parameters:
    my_list (list): The input list.
    item: The item to be appended.
    
    Returns:
    list: The modified list with the item appended.
    """
    my_list.append(item)
    return my_list

## Problem 2: Remove a specific item from a list
def remove_from_list(my_list, item):
    """
    Remove the first occurrence of a specific item from a list.
    
    Parameters:
    my_list (list): The input list.
    item: The item to be removed.
    
    Returns:
    list: The modified list with the item removed.
    """
    my_list.remove(item)
    return my_list

# Intermediate Problems:

## Problem 1: Reverse the order of elements in a list
def reverse_list(my_list):
    """
    Reverse the order of elements in a list.
    
    Parameters:
    my_list (list): The input list.
    
    Returns:
    list: The list with the elements in reverse order.
    """
    my_list.reverse()
    return my_list

## Problem 2: Find the index of an item in a list
def find_index(my_list, item):
    """
    Find the index of the first occurrence of a specific item in a list.
    
    Parameters:
    my_list (list): The input list.
    item: The item to search for.
    
    Returns:
    int: The index of the first occurrence of the item, or -1 if not found.
    """
    try:
        return my_list.index(item)
    except ValueError:
        return -1

## Problem 3: Insert an item at a specific index in a list
def insert_at_index(my_list, index, item):
    """
    Insert an item at a specific index in a list.
    
    Parameters:
    my_list (list): The input list.
    index (int): The index at which to insert the item.
    item: The item to be inserted.
    
    Returns:
    list: The modified list with the item inserted.
    """
    my_list.insert(index, item)
    return my_list