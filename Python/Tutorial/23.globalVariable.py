"""
LocalVariable:
A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

GlobalVariable:
A variable created in the main body of the Python code is a global variable and belongs to the global scope.

NOTE: To use a change or update a global variable from inside a function we need to use global keyword, also to create a global variable from inside a function we have to use the same.

def myfunc():
  global x
  x = 300

"""