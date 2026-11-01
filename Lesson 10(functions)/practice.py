def odd_or_even(numbers):
    if numbers % 2 == 0:
        return "even"
    else:
        return "odd"

def hypothenuse():
    a = int(input("enter the first side: "))
    b = int(input("enter the second side: "))
    c = (a ** 2 + b ** 2) ** 0.5
    return c

print(odd_or_even(5))
print(hypothenuse())