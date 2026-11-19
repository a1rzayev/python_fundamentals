class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

class Dog(Animal): #class1(class2) - class1 is a children(inheritenced) from class2
    def run(self):
        print(f"{self.name} is running")

dog = Dog("Max")
dog.eat() # children classes are able to access data of parent class
dog.run()

animal = Animal("Layka")
animal.eat()
# animal.run() # will not work! as parent class cant access data of children class