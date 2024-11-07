# Basic Problems:

## Problem 1: Read the contents of a file
def read_file(file_path):
    """
    Read the contents of a file.
    
    Parameters:
    file_path (str): The path to the file.
    
    Returns:
    str: The contents of the file.
    """
    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except IOError:
        print(f"Error: Unable to read file at {file_path}")
        return None

## Problem 2: Write data to a file
def write_to_file(file_path, data):
    """
    Write data to a file.
    
    Parameters:
    file_path (str): The path to the file.
    data (str): The data to be written to the file.
    """
    try:
        with open(file_path, "w") as file:
            file.write(data)
    except IOError:
        print(f"Error: Failed to write to file at {file_path}")

# Intermediate Problems:

## Problem 1: Append data to a file
def append_to_file(file_path, data):
    """
    Append data to a file.
    
    Parameters:
    file_path (str): The path to the file.
    data (str): The data to be appended to the file.
    """
    try:
        with open(file_path, "a") as file:
            file.write(data + "\n")
    except IOError:
        print(f"Error: Failed to append to file at {file_path}")

## Problem 2: Read a file line by line
def read_file_lines(file_path):
    """
    Read a file line by line.
    
    Parameters:
    file_path (str): The path to the file.
    
    Returns:
    list: A list of lines from the file.
    """
    try:
        with open(file_path, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return []
    except IOError:
        print(f"Error: Unable to read file at {file_path}")
        return []