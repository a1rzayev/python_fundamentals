# abc - module
# ABC allows us to create Abstract Base Classes
# abstractmethod - marks a method that children classes must implement
from abc import ABC, abstractmethod

class Animal(ABC): # create a child of Abstract Base Class to make it Abstract
    @abstractmethod # marks make_sound as an abtract method
    def make_sound(self):
        pass # the method has no implementation here

    @abstractmethod
    def move(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

    def move(self):
        print("run!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")
        
    def move(self):
        print("run!")

class Bird(Animal):
    def make_sound(self):
        print("Chik!")

    def move(self):
        print("fly!")


dog = Dog()
cat = Cat()
bird = Bird()

dog.make_sound()
cat.make_sound()
bird.make_sound()