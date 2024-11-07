"""
***NOTE: Adding an item to the dictionary is done by using a new index key and assigning a value to it:
eg:- 
Syntax: var[key] = value
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)


Dictionary Methods:

Method	        Description	                                Example
get(key, dflt)	Returns value for key; dflt if missing	    d.get('a', 0)
keys()	        Returns a view of keys	                    d.keys()
values()	    Returns a view of values	                d.values()
items()	        Returns a view of key-value pairs	        d.items()
update(dict2)	Updates dictionary with items from dict2	d.update({'b': 2})
pop(key)	    Removes key and returns value	            d.pop('a')
clear()         clear the entire dict at once               d.clear()
copy()          returns a copy of the specified dict.       d.copy()

"""

# NOTE: it's not optimum there can be more methods.

