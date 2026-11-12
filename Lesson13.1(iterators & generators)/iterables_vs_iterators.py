# Iterable - object which can return an iterator(lists, tuples, strings, dictionaries)
# Iterator - object that produces one at a time
numbers = [10, 20, 30, 40]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
# one more will give an StopIteration error

print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])
# one more will give an IndexError 

print(iterator is numbers) # False