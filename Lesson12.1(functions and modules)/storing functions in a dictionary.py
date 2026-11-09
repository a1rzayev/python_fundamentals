def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

operations = {"+" : add, "-" : subtract, "*" : multiply}

print(operations["+"](10, 5))
for symbol in operations:
    print(f"10 {symbol} 5 = {operations[symbol](10, 5)}")