
"""
https://medium.com/@euniceadewusic/python3-exploring-the-power-of-mutable-and-immutable-objects-452a3dd16be3
"""

#  type conversion
integer_number = 123
float_number = 1.23

new_num = integer_number + float_number

print(new_num)

num_string = '12'
num_integer = 23

new_sum = int(num_string) + num_integer
print(new_sum)

"""
- ID and Type:
In Python, each object has a unique identifier (ID) that represents its memory address. 
The built-in function id() provides this identifier, enabling us to verify whether two variables 
point to the same object. The type() function, on the other hand, helps us identify the type of 
an object, such as int, str, list, tuple, etc.
"""

# Mutable Data Types
"""
Mutable objects are those that can be modified after creation. Lists, dictionaries, 
and sets are examples of mutable objects in Python. When we modify a mutable object, 
such as appending an element to a list, the object itself is changed, but its ID remains the same.

- List
- Set
- Dictionary
"""





# Immutable Data Types
"""
Immutable objects, as the name suggests, cannot be altered after creation. 
Examples of immutable objects include integers, strings, and tuples. 
When we perform an operation on an immutable object, a new object is created with the 
updated value, preserving the original object’s integrity and the original object’s ID 
remains unchanged.

- Strings
- Integers
- Floating-pointing numbers
- Boolean
- Tuples
- Frozen sets
"""




