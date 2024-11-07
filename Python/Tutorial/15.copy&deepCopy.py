#Copying in Python refers to creating a new object with the same elements as an existing object. However, depending on whether the copy is shallow or deep, the copying process will treat nested elements differently.


"""

1) Shallow Copy (copy):
A shallow copy creates a new object that stores references to the same elements as the original. If the elements are mutable and contain further nested objects (like lists within lists), then changes to nested objects in the copied list will reflect in the original list too.
eg..
import copy

# Original list with a nested list inside
original = [[1, 2, 3], [4, 5, 6]]
shallow_copied = copy.copy(original)

# Modifying a nested list within the shallow copy
shallow_copied[0][0] = 99
print(original)  # Output: [[99, 2, 3], [4, 5, 6]] (original is affected)
print(shallow_copied)  # Output: [[99, 2, 3], [4, 5, 6]]

2) Deep Copy (deepcopy)
A deep copy creates a completely new object with its own copies of all nested objects, so no references to the original object remain. This ensures that changes in the deep-copied object do not affect the original, even with nested mutable objects.
eg..
# Creating a deep copy
deep_copied = copy.deepcopy(original)

# Modifying a nested list within the deep copy
deep_copied[0][0] = 42
print(original)  # Output: [[99, 2, 3], [4, 5, 6]] (original is unaffected)
print(deep_copied)  # Output: [[42, 2, 3], [4, 5, 6]]

"""
