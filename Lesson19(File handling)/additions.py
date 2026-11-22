"""count lines in a file"""

with open("students.txt", "r") as file:
    lines = file.readlines() # reading all lines into a list
print(f"lines count = {len(lines)}")



"""search for a name in file"""

search_name = input("enter student name: ")

with open("students.txt", "r") as file:
    content = file.read()

if search_name in content:
    print("Student found!")
else:
    print("Student not found!")



"""handle a missing file"""

try:
    with open("data.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("The file does not exist!")