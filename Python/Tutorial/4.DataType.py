"""Variables can store data of different types, and different types can do different things.
Python has the following data types built-in by default, in these categories:

1) Text Type:  str (strings are immutable.)
eg.. 
text = "Hello"
text[0] = "J"  # This will raise an error because strings are immutable

2) Numeric Types:  int, float, complex (eg.. "complex_number = 3 + 4j" where  realpart is 3 & imaginary part is 4j) 

3) Sequence Types:	list (mutable,ordered), tuple(immutable,ordered), range(ordered,immutable)

4) Mapping Type:	dict ( is an unordered, mutable collection of key-value pairs. Each key must be unique and immutable)

5) Set Types:	set (An unordered, mutable collection of unique elements), frozenset
(An immutable version of a set, 
eg.. 
frozen_fruits = frozenset(["apple", "banana", "cherry"])
print(frozen_fruits)  # Output: frozenset({'apple', 'banana', 'cherry'})
)

6) Boolean Type:	bool (The bool type represents a Boolean value, which can be either True or False. Boolean values are often used for conditional statements and logic)

7) Binary Types:	bytes(Represents a sequence of immutable bytes (8-bit values). Useful for binary data like files, images, and network packets. 
eg.. 
byte_data = b"Hello"
print(type(byte_data))), 

bytearray(Similar to bytes, but mutable. You can modify the elements after creation. eg.. 
mutable_data = bytearray(b"Hello")
mutable_data[0] = 74  # ASCII code for 'J'
print(mutable_data)    # Output: bytearray(b'Jello')), 
 
memoryview (Provides a way to access the memory of an object without copying it. Useful for efficient manipulation of large binary data. 
eg.. 
data = bytearray(b"abcdefgh")
mem_view = memoryview(data)
# Access a slice without copying
slice_view = mem_view[2:6]   # Only refers to 'cdef' without making a new copy
slice_view[0] = ord('X')     # Modify within the slice
print(data)                  # Output: bytearray(b"abXefgh")
)

8) None Type:	NoneType(The NoneType has a single value, None, which represents the absence of a value or a null value.)"""

#You can get the data type of a variable with the type() function. 
x = 5
y = "John"
print(type(x))
print(type(y))


