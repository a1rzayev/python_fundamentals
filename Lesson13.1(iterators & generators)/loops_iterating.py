numbers = [1, 2, 3, 4, 5, 6]

iterator = iter(numbers)

while True:
    try:
        value = next(iterator)
        print(value)
    except StopIteration:
        break