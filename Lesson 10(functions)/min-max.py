# min and max

def my_min(numbers):
    if numbers == False:
        return "no numbers in list!"
    minimum_number = numbers[0]
    for element in numbers:
        if element < minimum_number:
            minimum_number = element
    return minimum_number

def my_max(numbers):
    if numbers == False:
        return "no numbers in list!"
    maximum_number = numbers[0]
    for element in numbers:
        if element > maximum_number:
            maximum_number = element
    return maximum_number

def min_max(numbers):
    return my_min(numbers), my_max(numbers)


my_numbers = [7, 8, 9, 1, 4, 6, 11, 13]

print(min_max(my_numbers))


