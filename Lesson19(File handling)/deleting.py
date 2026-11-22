"""check if a file exists"""

import os # Operational System

if os.path.exists("teachers.txt"):
    print("File exists")
else:
    print("File does not exist:(")



"""deleting a file"""

if os.path.exists("example.txt"):
    os.remove("example.txt")
    print("file deleted!")
else:
    print("file not found!")

# os.remove("test.txt") # FileNotFoundError