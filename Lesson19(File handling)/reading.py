"""entire file"""

with open("example.txt", "r") as file:
    content = file.read() # reading entire file
print(content, "\n\n")



"""one line"""

with open("example.txt", "r") as file:
    first_line = file.readline() # reading one line from file
print(first_line, "\n\n")



"""all lines into a list"""

with open("example.txt", "r") as file:
    lines = file.readlines() # reading all lines into a list
print(lines, "\n\n")



"""all lines into a list""" # alternate method

with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())