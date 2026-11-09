try:
    file = open("data.txt", "r")
    print(file.read())
    file.close()

except FileNotFoundError:
    print("file not found!")

finally: # executes no matter what happenned
    print("program finished!")




"""best type of file working"""

try:
    with open("data.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("file not found!")