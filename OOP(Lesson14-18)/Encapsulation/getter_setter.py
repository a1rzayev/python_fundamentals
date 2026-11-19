class Student:
    def __init__(self, grade):
        self.__grade = grade

    def get_grade(self): # getter
        return self.__grade
    
    def set_grade(self, grade): # setter
        if( 0 <= grade and grade <= 100):
            self.__grade = grade
        else:
            print("Invalid grade!")

Muradkhan = Student(95)

print(f"Grade: {Muradkhan.get_grade()}")

Muradkhan.set_grade(100)

print(f"Grade: {Muradkhan.get_grade()}")