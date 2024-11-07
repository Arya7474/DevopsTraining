"""
1) Concatenation:
   -> Concatenation with +: Combines strings directly.
      eg:-
      greeting = "Hello" + ", World!"
      print(greeting)
"""

"""
2) String Formatting:
- f-strings: Easier and more readable for embedding expressions directly.
  eg:- 
  name = "Alice"
  age = 25
  print(f"My name is {name} and I'm {age} years old.")

- format() method: Allows for more complex formatting options.
  eg:-
  print("Hello, {}!".format("World"))

"""

"""
3) String Methods:

Method	        Description	                              Example
upper()	        Converts to uppercase	                    'hello'.upper() → 'HELLO'
lower()	        Converts to lowercase	                    'Hello'.lower() → 'hello'
strip()	        Removes whitespace from start/end	        ' Hello '.strip() → 'Hello'
replace(a, b)	  Replaces substring a with b	              'hello'.replace('e', 'a') → 'hallo'
find(sub)	      Returns index of sub, -1 if not found	    'hello'.find('e') → 1
split(sep)	    Splits string by sep into a list	        'a,b,c'.split(',') → ['a', 'b', 'c']

"""

# NOTE: it's not optimum there can be more methods.