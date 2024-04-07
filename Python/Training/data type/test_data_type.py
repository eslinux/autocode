# In Python, there are several basic data types that are commonly used:
# Integer (int): Represents whole numbers, both positive and negative, without fractional parts. For example: 0, 42, -10.
# Floating-Point Number (float): Represents real numbers with decimal points. For example: 3.14, -0.5, 2.0.
# Boolean (bool): Represents either True or False. Booleans are often used in logical operations and control flow. For example: True, False.
# String (str): Represents a sequence of characters enclosed in single quotes ('...') or double quotes ("..."). For example: 'Hello', "Python", '123'.
# List (list): Represents an ordered collection of elements, which can be of different types. Lists are mutable, meaning their elements can be modified. For example: [1, 2, 3], ['apple', 'banana', 'cherry'].
# Tuple (tuple): Similar to a list, but tuples are immutable, meaning their elements cannot be modified once created. Tuples are typically written with parentheses (...) or without any delimiters. For example: (1, 2, 3), 'a', 'b', 'c'.
# Dictionary (dict): Represents an unordered collection of key-value pairs. Each key must be unique within a dictionary. Dictionaries are enclosed in curly braces {}. For example: {'name': 'John', 'age': 25, 'city': 'New York'}.
# Set (set): Represents an unordered collection of unique elements. Duplicates are automatically removed in a set. Sets are enclosed in curly braces {}. For example: {1, 2, 3}, {'apple', 'banana', 'cherry'}.
# These are the basic data types in Python, and they can be used to store and manipulate different kinds of data in your programs. Python also provides more advanced data types and data structures through modules and libraries.



#List
my_list = list() # or []
my_list.append(1)
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append("hihi")
print(my_list) #[1, 1, 2, 3, 4, 'hihi']


#Set
my_set = set() #or {}
my_set.add(1)
my_set.add(1)
my_set.add(2)
my_set.add(3)
my_set.add(4)
my_set.add("hihi")
print(my_set) #{1, 2, 3, 4, 'hihi'}


#Dict
my_dict = dict()
my_dict["name"] = "jack"
my_dict["age"] = 25
my_dict["is_ok"] = True
print(my_dict) #{'name': 'jack', 'age': 25, 'is_ok': True}
