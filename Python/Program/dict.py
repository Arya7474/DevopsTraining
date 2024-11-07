# Basic Problems:

## Problem 1: Add a key-value pair to a dictionary
def add_to_dict(my_dict, key, value):
    """
    Add a new key-value pair to a dictionary.
    
    Parameters:
    my_dict (dict): The input dictionary.
    key: The key to be added.
    value: The value to be associated with the key.
    
    Returns:
    dict: The modified dictionary with the new key-value pair.
    """
    my_dict[key] = value
    return my_dict

## Problem 2: Remove a key-value pair from a dictionary
def remove_from_dict(my_dict, key):
    """
    Remove a key-value pair from a dictionary.
    
    Parameters:
    my_dict (dict): The input dictionary.
    key: The key to be removed.
    
    Returns:
    dict: The modified dictionary with the key-value pair removed.
    """
    if key in my_dict:
        del my_dict[key]
    return my_dict

# Intermediate Problems:

## Problem 1: Get the keys or values of a dictionary as a list
def get_keys_values(my_dict):
    """
    Get the keys and values of a dictionary as separate lists.
    
    Parameters:
    my_dict (dict): The input dictionary.
    
    Returns:
    Tuple[list, list]: A tuple containing the list of keys and the list of values.
    """
    return list(my_dict.keys()), list(my_dict.values())

## Problem 2: Merge two dictionaries
def merge_dicts(dict1, dict2):
    """
    Merge two dictionaries into a new dictionary.
    
    Parameters:
    dict1 (dict): The first dictionary.
    dict2 (dict): The second dictionary.
    
    Returns:
    dict: The merged dictionary.
    """
    result = {**dict1, **dict2}
    return result

## Problem 3: Get the most common key-value pairs in a dictionary
from collections import Counter

def most_common_pairs(my_dict):
    """
    Get the most common key-value pairs in a dictionary.
    
    Parameters:
    my_dict (dict): The input dictionary.
    
    Returns:
    list: A list of the most common key-value pairs.
    """
    return Counter(my_dict.items()).most_common()