"""
The try block lets you test a block of code for errors.
The except block lets you handle the error.
The else block lets you execute code when there is no error.
The finally block lets you execute code, regardless of the result of the try- and except blocks.

*Why we need try, except??
ANS: Exception Handling
When an error occurs, or exception as we call it, Python will normally stop and generate an error message.
These exceptions can be handled using the try statement:

Example:
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    else:
        print("Division successful. Result is:", result)
    finally:
        print("Execution complete.")

# Test with different values
divide(10, 2)  # Should print success message
divide(10, 0)  # Should print error message

try block: Contains code that might raise an exception (a / b).
except block: Catches the ZeroDivisionError if it occurs.
else block: Executes if no exception is raised, and the division is successful.
finally block: Runs whether an exception occurs or not (useful for cleanup like closing files).

 
** raise:
The raise keyword is used to manually raise an exception. You can raise exceptions based on certain conditions in your program.
try:
    age = -5  # Invalid age
    if age < 0:
        raise ValueError("Age cannot be negative.")
except ValueError as e:
    print(f"Error: {e}")

"""

