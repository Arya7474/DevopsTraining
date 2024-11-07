# Basic Problems:

## Problem 1: Access and modify a global variable
GLOBAL_CONSTANT = 42

def access_global_constant():
    """
    Access and return the value of the global constant.
    
    Returns:
    int: The value of the global constant.
    """
    return GLOBAL_CONSTANT

def modify_global_constant(new_value):
    """
    Modify the value of the global constant.
    
    Parameters:
    new_value (int): The new value for the global constant.
    """
    global GLOBAL_CONSTANT
    GLOBAL_CONSTANT = new_value

# Intermediate Problems:

## Problem 1: Create a global variable and use it in multiple functions
GLOBAL_LIST = []

def add_to_global_list(item):
    """
    Add an item to the global list.
    
    Parameters:
    item: The item to be added to the global list.
    """
    global GLOBAL_LIST
    GLOBAL_LIST.append(item)

def print_global_list():
    """
    Print the contents of the global list.
    """
    global GLOBAL_LIST
    print(GLOBAL_LIST)

## Problem 2: Understand the scope of global and local variables
def local_variable_example():
    """
    Demonstrate the scope of local variables.
    """
    local_variable = 10
    print(f"Inside the function, local_variable is: {local_variable}")

def global_variable_example():
    """
    Demonstrate the scope of global variables.
    """
    print(f"Outside the function, GLOBAL_CONSTANT is: {GLOBAL_CONSTANT}")
    
    def inner_function():
        """
        Demonstrate accessing the global variable from within a nested function.
        """
        print(f"Inside the inner function, GLOBAL_CONSTANT is: {GLOBAL_CONSTANT}")
    
    inner_function()