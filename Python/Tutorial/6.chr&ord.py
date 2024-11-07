#The chr() and ord() functions in Python are built-in functions for working with ASCII and Unicode characters.

# what is ascii & unicode ?? -> ASCII and Unicode are character encoding standards used to represent text in computers, where each character is assigned a unique number. While ASCII is more limited and older, Unicode is a modern, comprehensive standard that includes characters from many languages and symbols.

"""
Function	Purpose	                                                  Example Usage	    Output
chr()	    Converts an integer (Unicode or ascii) to a character	  chr(65)	        'A'
ord()	    Converts a character to its integer Unicode code point	  ord('A')	        65

"""

# usecase:
# Generate a list of uppercase letters A-Z
uppercase_letters = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
print(uppercase_letters)
# Output: ['A', 'B', 'C', ..., 'Z']

