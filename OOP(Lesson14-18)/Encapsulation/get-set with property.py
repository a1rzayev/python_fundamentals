class Student:
    def __init__(self, grade):
        self.__grade = grade

    @property
    def grade(self):
        return self.__grade
    
    @grade.setter
    def grade(self, value):
        if( 0 <= value <= 100):
            self.__grade = value
        else:
            print("Invalid grade")


Ali = Student(85)

print(Ali.grade)

Ali.grade = 95

print(Ali.grade)