#NOTE: indexing and slicing only works in collection datatypes.

#Indexing
"""
Indexing is the process of accessing an element in a sequence using its position in the sequence (its index).

In Python, indexing starts from 0, which means the first element in a sequence is at position 0, the second element is at position 1, and so on.

To access an element in a sequence, you can use square brackets [] with the index of the element you want to access.

Let's consider the following example:
my_list = ['apple', 'banana', 'cherry', 'date']
print(my_list[0]) # output: 'apple'
print(my_list[1]) # output: 'banana'

Indexing is two types: Positive and Negative Indices
Positive indices start from 0 and increase from the left.
Negative indices start from -1 and go leftward.
"""

#Slicing
"""
Slicing
Slicing is a technique for extracting a portion (or "slice") of a sequence like a string, list, or tuple by specifying a start, stop, and step.

Syntax
sequence[start:stop:step]

start: The index where slicing begins.
stop: The index where slicing ends.
step: The number of indices to skip.

example:
text = "Hello, World!"
# Positive indices
print(text[0:5])  # 'Hello' - start at index 0, end at index 5 
print(text[:5])   # 'Hello' - omitting start defaults to 0
print(text[7:12]) # 'World' - start at index 7, end at index 12

# Negative indices
print(text[-6:-1])  # 'World' - start from index -6 to -1
print(text[-6:])    # 'World!' - omitting stop takes until end of string

# Using step
print(text[::2])    # 'Hlo ol!' - every 2nd character from start to end
print(text[::-1])   # '!dlroW ,olleH' - reverses string by using -1 step

"""



