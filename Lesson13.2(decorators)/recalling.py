"""Assign function to a variable"""

def greet():
    print("Hello everyone!")

message = greet # assigning function to a variable

#no difference will be
message()
greet()



"""Passing a function as an argument"""

def say_hello():
    print("hello")

def execute_other_function(func):
    func()

execute_other_function(say_hello)


