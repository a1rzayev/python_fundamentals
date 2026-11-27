import sqlite3

class Student:
    def __init__(self, name, birth_year, city):
        self.name = name
        self.birth_year = birth_year
        self.city = city

    def speak():
        print("I am speaking...")


name = input("Enter your name: ")
birth_year = int(input("Enter your birthyear: "))
city = input("Enter your city of residence: ")

student = Student(name, birth_year, city)



connection = sqlite3.connect("students.db")

cursor = connection.cursor()

cursor.execute("""
INSERT INTO students (name, birth_year, city)
VALUES(?, ?, ?)
""", (student.name, student.birth_year, student.city))

connection.commit()

cursor.execute("SELECT * FROM students")

students = cursor.fetchall()

for stud in students:
    print(stud)

connection.close() # closing your connection(session) to db


# '*' - everything / multiple elements
# '?' - one element