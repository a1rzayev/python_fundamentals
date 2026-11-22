# opens if exist, if not - creates one
# w - "write": formats file content and starts from empty sheet
# a - "append": appends(adds) to the file content from the end of it
# r - "read": only shows content without modifiing

with open("example.txt", "w") as file: # w - write, a - append, r - reading
    file.write("Hello students\n")
    file.write("Hello teacher\n")
    file.write("Have you done your homework?\n")
    file.write("Yes sure\n")
    file.write("Today is file-handling day!")

print("File created successfully")