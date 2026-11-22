"""appending new information"""

with open("example.txt", "a") as file:
    file.write("\nToday we learned file handling!")

print("New information added successfully!")



"""overwriting existing info"""

with open("example.txt", "w") as file:
    file.write("This is the new content")



"""writing multiple lines"""
students = ["Muradkhan", "Ali", "Hasan", "Fateh", "Rafael"]

with open("students.txt", "w") as file:
    for student in students:
        file.write(student + "\n")

