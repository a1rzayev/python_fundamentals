import sys 

numbers_list = [x * x for x in range(1000000)] # list
numbers_generator = (x * x for x in range(100000)) # generator(more optimized for bigger data)

print(sys.getsizeof(numbers_list)) # checking size
print(sys.getsizeof(numbers_generator)) # checking size