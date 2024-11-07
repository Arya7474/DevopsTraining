"""Typecasting in Python is the process of converting a variable from one data type to another.
Types of Typecasting:
Implicit Typecasting (Automatic Conversion)
Explicit Typecasting (Manual Conversion)"""

# 1) Implicit Typecasting
int_num = 5       # Integer
float_num = 2.5   # Float

# Adding integer and float results in a float
result = int_num + float_num
print(result)          # Output: 7.5
print(type(result))    # Output: <class 'float'>

"""In this example, int_num is automatically converted to a float when added to float_num, so the result is also a float. This type of typecasting is seamless and done by Python without any instruction."""

# 2) Explicit Typecasting
""" Common Explicit Typecasting Functions and therir use cases:
eg..
Function	ConvertsTo	 Example                     Output
int()	    Integer	     int("10")	                 10
float()	    Float	     float("10.5")	             10.5
str()	    String	     str(123)	                 "123"
bool()	    Boolean	     bool(0)	                 False
list()	    List	     list("abc")	             ['a', 'b', 'c']
tuple()	    Tuple	     tuple([1, 2, 3])	         (1, 2, 3)
set()	    Set	         set([1, 2, 2, 3])	         {1, 2, 3}
dict()	    Dictionary	 dict([("a", 1), ("b", 2)])	 {'a': 1, 'b': 2} # NOTE: Converts a sequence of key-value pairs (e.g., a list of tuples) to a dictionary.
bytes()	    Bytes	     bytes("hello", "utf-8")	 b'hello'

"""