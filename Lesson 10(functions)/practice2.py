def add(*args):
    sum = 0
    for elem in args:
        sum += elem
    return sum

def multiply(*args):
    product = 1
    for elem in args:
        product *= elem
    return product
    
print(add(10, 14, 15, 12))
print(multiply(4, 1, 2, 7))
 