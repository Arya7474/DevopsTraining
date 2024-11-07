"""
A function is a block of code which only runs when it is called.
You can pass data, known as parameters, into a function.
A function can return data as a result.

1) Creating a Function(function defination)
In Python a function is defined using the def keyword:
def my_function():
  print("Hello from a function")

2) Calling a Function(Function Call)
To call a function, use the function name followed by parenthesis:
def my_function():
  print("Hello from a function")

my_function()

3) return in a Function:
The return statement is used to exit a function and pass a value back to the caller. It allows you to send back the result of a function's execution.

def function_name():
    # some code
    return value

NOTE: The function stops execution once return is encountered, in other words it works as break.
Example:
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # Output: 8
"""

