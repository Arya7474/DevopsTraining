# Basic Problems:

## Problem 1: Split a string into a list of words
def split_to_words(string):
    """
    Split a string into a list of words.
    
    Parameters:
    string (str): The input string.
    
    Returns:
    list: A list of words from the input string.
    """
    return string.split()

## Problem 2: Join a list of strings into a single string
def join_strings(string_list, separator):
    """
    Join a list of strings into a single string using a specified separator.
    
    Parameters:
    string_list (list): The list of strings to be joined.
    separator (str): The separator to use between the strings.
    
    Returns:
    str: The joined string.
    """
    return separator.join(string_list)

# Intermediate Problems:

## Problem 1: Split a string on multiple delimiters
def split_on_multiple(string, delimiters):
    """
    Split a string on multiple delimiters and return a list of substrings.
    
    Parameters:
    string (str): The input string.
    delimiters (str): The delimiters to split the string on (e.g. ", " or ";\t").
    
    Returns:
    list: A list of substrings from the input string.
    """
    return string.split(f"[{delimiters}]", string)

## Problem 2: Join a list of numbers into a string with a custom separator
def join_numbers(number_list, separator):
    """
    Join a list of numbers into a string using a specified separator.
    
    Parameters:
    number_list (list): The list of numbers to be joined.
    separator (str): The separator to use between the numbers.
    
    Returns:
    str: The joined string of numbers.
    """
    return separator.join(map(str, number_list))

## Problem 3: Split a CSV string into a list of dictionaries
import csv

def csv_to_dicts(csv_string):
    """
    Split a CSV string into a list of dictionaries, where the keys are the column headers.
    
    Parameters:
    csv_string (str): The input CSV string.
    
    Returns:
    list: A list of dictionaries, where each dictionary represents a row in the CSV.
    """
    reader = csv.DictReader(csv_string.splitlines())
    return list(reader)