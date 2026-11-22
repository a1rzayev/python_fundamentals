class Dog: # user-defined data type(class)
    def speak(self):
        print("Woof!")

class Cat:
    def speak(self):
        print("Meow!")

class Cow:
    def speak(self):
        print("Moo!")

layka = Dog() # object - variable of class
musya = Cat()
dusya = Cow()

layka.speak()
musya.speak()
dusya.speak()

animals_list = [Dog(), Cat(), Cow()] # the same

for animal in animals_list:
    animal.speak()