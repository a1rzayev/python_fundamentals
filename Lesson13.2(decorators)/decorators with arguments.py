# decorator - function which takes another function and extends/modifies it without changing original source code

# *something = [1, 2, 3, 4, 5...]
# **something = [(1, 1), (2, 2), (3, 3)...]

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function execution")

        result = func(*args, **kwargs)

        print("After function execution")
        
        return result
    return wrapper

@my_decorator
def add(a, b):
    return a + b 

print(add(5, 10))