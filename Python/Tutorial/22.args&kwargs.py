"""
1) paxking & unpacking:
Packing:
Packing is the process of collecting multiple values into a single data structure, like a tuple or list. In Python, this happens automatically when you pass multiple arguments into a function.
For example, when you pass arguments to a function, they are packed into a tuple if you use *args
def example(*args):
    print(args)  # args is a tuple containing all the passed values

example(1, 2, 3)  # Packing into a tuple (1, 2, 3)


Unpacking:
Unpacking is the reverse process, where you take a collection (tuple, list, or dictionary) and assign its individual elements to variables. This is useful when you want to extract values from an iterable and assign them to variables in a structured way.

For example, when you want to unpack values from a tuple into individual variables:
my_tuple = (1, 2, 3)
a, b, c = my_tuple  # Unpacking the tuple into individual variables
print(a, b, c)  # Output: 1 2 3

2) args & kwargs:
args is a common name for the variable that holds all positional arguments when using *.
kwargs stands for "keyword arguments," and it allows a function to accept a variable number of keyword arguments (i.e., named arguments).

Using *args:
As already explained, *args collects all positional arguments into a tuple.

Using **kwargs:
The ** syntax collects keyword arguments (named arguments) into a dictionary. This is useful when you don't know in advance how many named arguments will be passed to your function.
Syntax:
def function_name(**kwargs):
    # code
Example:
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_kwargs(name="John", age=25)  # Output: name: John  age: 25
Here, **kwargs collects the keyword arguments into a dictionary.

"""



