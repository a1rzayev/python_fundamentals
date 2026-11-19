class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name}")
        print(f"My age is {self.age}")

class Student(Person):
    pass

class Teacher(Person):
    pass

student = Student("Muradkhan", 16)
teacher = Teacher("Asif", 20)

student.introduce()
teacher.introduce()