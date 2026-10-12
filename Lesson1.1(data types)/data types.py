"""Numeric data types in Python"""
# int(integer) - whole numbers
x = 5 

# float - decimal numbers
y = 8.5

# complex number 
z = 2 + 3j



"""Boolean data type in Python"""
# bool - True or False(0 - false, anything except 0 - true)
is_active = True



"""String data type in Python"""
# str - sequence of characters
name = "Asif"

print(name[1]) # indexing from start(starting from 0)
print(name[-3]) # indexing from end(starting from -1)



"""Binary types in Python"""
# bytes - immutable sequence of bytes
FIN = b"3M8GHJK"

#bytearray - mutable sequence of bytes
licence_plate = bytearray(b"10AB100")

#memoryview - memory view object of a bytes-like object
car_memory = memoryview(licence_plate)



"""Sequence data types in Python"""
# list - ordered, mutable collection of items
fruits = [1, "banana", b"apple", 2.5, False]

print(fruits)
fruits.append("mango")
print(fruits)

# tuple - ordered, immutable collection of items
fruits_tuple = (16, "Muradxan", 1.91)

# range - ordered, immutable sequence of numbers
numbers = range(5, 10)



"""Set data types in Python"""
# set - unordered, mutable collection of unique items
fruits_set = {"banana", "apple", "mango", "banana"}
print(fruits_set)

# frozenset - unordered, immutable collection of unique items
fruits_frozenset = frozenset({"banana", "apple", "mango", "banana"})



"""Dictionary data type in Python"""
# dict - unordered, mutable collection of key-value pairs
cars_dict = {"10AB123": "BYD", "10BA456": "Toyota", "10BA456": "Honda"}

print(cars_dict["10BA456"]) 



"""None data type in Python"""
# NoneType - represents the absence of a value or a null value
car = None
cars_dict["10BC789"] = car


print(cars_dict)