students = {"1234":["Murad", 16, "ADA", "Business"], "23456": ["Ali", 16, "MedUni", "Medicine"]}

# first way(using nested FOR)
for student in students:
    print("ID:", student)
    for elem in students[student]:
        print("*", elem)
    print()

# second way(using manually printing each element in VALUE)
for student in students:
    print("ID:", student)
    print("Name:", students[student][0])
    print("Age:", students[student][1])
    print("University:", students[student][2])
    print("Major:", students[student][3])
    print()