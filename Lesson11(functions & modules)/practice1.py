def countdown(n):
    if(n == 0):
        print("Start!")
        return #empty return - just finishes the function
    print(n)
    countdown(n - 1)
    

countdown(5)