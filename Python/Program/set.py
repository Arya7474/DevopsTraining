# Basic Problems:

## Problem 1: Add items to a set
def add_to_set(my_set, *items):
    """
    Add one or more items to a set.
    
    Parameters:
    my_set (set): The input set.
    *items: The items to be added to the set.
    
    Returns:
    set: The modified set with the new items added.
    """
    for item in items:
        my_set.add(item)
    return my_set

## Problem 2: Remove an item from a set
def remove_from_set(my_set, item):
    """
    Remove a specific item from a set.
    
    Parameters:
    my_set (set): The input set.
    item: The item to be removed.
    
    Returns:
    set: The modified set with the item removed.
    """
    my_set.remove(item)
    return my_set

