with open("students.txt", "r") as file:
    print(file.read(5)) # until fifth character 5 => (0, 4)

    print("Current position:", file.tell()) # tell() shows the current position in the file

    file.seek(0) # seek() moves to the position of providen index 

    print("After moving:", file.tell())

    print(file.read())
