try:
    number = int(input("input a number:"))
    result = 100 / number

# except: # bad practice
#     print("something went wrong!")

except ValueError:
    print("please enter a valid number")

except ZeroDivisionError:
    print("please do not enter 0")

else: # executes only if no other(error) was executed
    print("Result:", result)