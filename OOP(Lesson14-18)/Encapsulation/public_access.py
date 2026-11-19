# public - accessable and modifyable directly from everywhere
class Person:
    def __init__(self, name):
        self.name = name

student = Person("Muradkhan")
teacher = Person("Asif")

print(f"Student: {student.name}")
print(f"Teacher: {teacher.name}")

student.name = "Ali"
teacher.name = "Mamed"

print(f"Student: {student.name}")
print(f"Teacher: {teacher.name}")