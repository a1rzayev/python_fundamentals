# decorator - function which takes another function and extends/modifies it without changing original source code

def my_decorator(func):
    def wrapper():
        print("Before function execution")

        func()

        print("After function execution")
    return wrapper

@my_decorator #1st way 
def say_hello():
    print("Hello!")

say_hello = my_decorator(say_hello) # 2nd way
say_hello()

@my_decorator
def fibonacci(n):
    pass