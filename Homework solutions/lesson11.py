def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def divide(a, b):
    return a / b
def multiply(a, b):
    return a * b
def evaluate(a, operation, b):
    functions = {
        "+": add,
        "-": subtract,
        "/": divide,
        "*": multiply
    }

    if operation not in functions:
        return "wrong operation"
    return functions[operation](a, b)

x = float(input("Enter X: "))
operation = input("Enter operation (+, -, /, *): ")
y = float(input("Enter Y: "))
 
print(evaluate(x, operation, y))