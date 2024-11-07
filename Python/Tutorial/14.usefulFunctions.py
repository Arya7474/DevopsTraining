"""
1) join() Method
This method takes all items in an iterable and joins them into one string.
Syntax: separator.join(iterable)

#Joining a list of words with a space as a separator
words = ["Hello", "world", "from", "Python"]
sentence = " ".join(words)
print(sentence)  # Output: "Hello world from Python"

2) len() method
The len() function returns the length of an object, which could be a string, list, tuple, or any other collection type.
eg..
text = "Hello, world!"
print(len(text))  # Output: 13

3) isalnum() method
The isalnum() method checks if all characters in the string are alphanumeric (either alphabet letters or numbers) and returns True if they are, False otherwise.
eg..
text = "Hello123"
print(text.isalnum())  # Output: True

text = "Hello 123"
print(text.isalnum())  # Output: False (contains a space)

4) isalpha() Method
The isalpha() method checks if all characters in the string are alphabetic (letters only) and returns True if they are, False otherwise.

5) isnumeric() Method
The isnumeric() method checks if all characters in the string are numeric, including digits and other numeric characters (e.g., superscripts, fractions). It returns True if they are, False otherwise.

6) isdigit() Method
The isdigit() method is similar to isnumeric() but more restrictive, focusing on Unicode characters that are strictly considered digits (0-9 only). It returns True if all characters are digits, False otherwise.

7) isdecimal() Method
The isdecimal() method checks if all characters in the string are decimal characters. It is even more restrictive than isdigit(), as it only considers basic digits (0-9), without superscripts or fractions.

8) islower() Method
The islower() method checks if all alphabetic characters in the string are lowercase and returns True if they are. If the string has no alphabetic characters, it returns False.

9) isupper() Method
The isupper() method checks if all alphabetic characters in the string are uppercase and returns True if they are.

10) istitle() Method
The istitle() method checks if the string follows title case (i.e., each word starts with an uppercase letter followed by lowercase letters). It returns True if it does, False otherwise.

11) startswith() and endswith() Method
startswith(substring): Checks if the string begins with a specified substring.
endswith(substring): Checks if the string ends with a specified substring.
eg..
text = "Hello, World!"
print(text.startswith("Hello"))  # Output: True
print(text.endswith("!"))       # Output: True

12) sort() Method
In-place sorting: It sorts the list itself without creating a new list.
Only for lists: It is a list method and can only be used with lists.
No return value: It modifies the list in place and returns None

13) sorted() Method
Creates a new sorted list: It returns a new list with the sorted elements.
Works with any iterable: Can sort other types of iterables (like tuples, sets, or dictionaries).
Returns a sorted list: The original iterable remains unchanged

14) index() Method
find the index of an element in a list.
Syntax:
list.index(element)

eg..
my_list = ['apple', 'banana', 'cherry', 'date']
# Find the index of 'banana'
index_of_banana = my_list.index('banana')
print(index_of_banana)  # Output: 1

"""