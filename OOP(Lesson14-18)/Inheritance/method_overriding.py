class Animal:
    def make_sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def make_sound(self): # overriding
        print("Woof!")

class Cat(Animal):
    def make_sound(self): # overriding
        print("Meow!")

class Bird(Animal):
    pass

animal = Animal()
dog = Dog()
cat = Cat()
bird = Bird()

animal.make_sound()
dog.make_sound()
cat.make_sound()
bird.make_sound()