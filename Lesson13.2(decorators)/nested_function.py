def outer():
    message = "Hello. I am from outer function"

    def inner():
        print(message)
    
    return inner

my_function = outer()

my_function()