students = {"1234": ["Ali", 18, "ADA", "Math"], "456":["Mammed", 19, "UFAZ", "Science"], "4940":["Kamal", 21, "MedUni", "cargiology"], "1093":["Ayan", 20, "ADA", "Architecture"]}

for elem in students:
    if students[elem][2] == "ADA":
        print("student", elem, "is allowed")
    else:
        print("student", elem, "is not allowed")
        continue

 