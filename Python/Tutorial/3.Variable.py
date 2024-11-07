#Variables are containers for storing data values.
#A variable is created the moment you first assign a value to it.

a=10
#here "a" is variable name and the right side value "10" is assigned to variable a.
print(a) #upon printing "a" we get the value "10".

""" 
Variable Names:- 
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). 
Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords."""

#Python allows you to assign values to multiple variables in one line:
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
#And you can assign the same value to multiple variables in one line:
x = y = z = "Orange"
print(x)
print(y)
print(z)

#Unpack a Collection
#If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
#Unpack a list:
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
#******NOTE: Your task is to do the same in tuple , set , dict. 





