"""

#####
Python supports the usual logical conditions from mathematics:
Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
#####

1) if Statement:
The if statement evaluates a condition. If the condition is True, the block of code inside the if statement is executed. If it's False, it moves to the next condition (if available).
Syntax:
if condition:
    # code to execute if condition is True
Example:
age = 18
if age >= 18:
    print("You are an adult")

    
2) elif (else if) Statement:
elif allows you to check multiple conditions after an initial if statement. If the if condition is False, Python will check each elif condition one by one until it finds one that's True. If none of the conditions are True, the else block (if present) will be executed.
Syntax:
if condition_1:
    # code to execute if condition_1 is True
elif condition_2:
    # code to execute if condition_1 is False and condition_2 is True
elif condition_3:
    # code to execute if condition_1 and condition_2 are False, and condition_3 is True
else:
    # code to execute if none of the above conditions are True
Example:
age = 16
if age >= 18:
    print("You are an adult")
elif age >= 13:
    print("You are a teenager")
else:
    print("You are a child")


3) Ternary Operator (Conditional Expression):
The ternary operator is a compact way to write simple if-else statements in a single line, NOTE: its best used case is in a simple if-else without multi stage.
Syntax:
value_if_true if condition else value_if_false

age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)

"""
