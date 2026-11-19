class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, university):
        super().__init__(name, age) #super() - calling parent(Person) class
        self.university = university

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"University: {self.university}")

student = Student("Amirali", 20, "UFAZ")

student.display_info()