class Father:
    def skills(self):
        print("driving")

    # def hobbies(self): # will overlap "hobbies()" method of Mother
    #     print("football")

class Mother:
    def hobbies(self):
        print("painting")

class Child(Father, Mother): # multiple inheritance
    pass

child = Child()

child.skills()
child.hobbies()