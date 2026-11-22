import json # Java Script Object Notation

student = {
    "name": "Muradkhan",
    "surname": "Mammadov",
    "age": 16,
    "course": "Python",
    "FIN": "XXXXXXX"
}

"""writing"""

with open("student.json", "w") as file:
    json.dump(student, file, indent=4) # save python data into json file

# json.dumps - save python data into json string



"""reading"""

with open("student.json", "r") as file:
    student = json.load(file) # reads python data from json file

# json.loads - reads python data from json string

print(student)
print(student["name"])
print(student["course"])