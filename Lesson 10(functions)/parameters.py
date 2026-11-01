def hypothenuse(a=3, b=4): # default parameter
    c = (a ** 2 + b ** 2) ** 0.5
    return c

print(hypothenuse(6, 8))


def add(a, b, c = 3):
    return a + b + c

print(add(1, 2), add(1, 2, 3))