students = {"Muradkhan": "Representative", "Asif": "Student", "Aysel": None, "Nigar": "", "Ramin": "Student", "Rashad": None, "Tural": None, "Vusal": None}


for student in students:
    if(students[student] != None and len(students[student]) > 0):
        print(student, "is a ", students[student])
    else:
        print(student, "is not a standart user")