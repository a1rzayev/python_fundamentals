class Callable:
    def call(self):
        print("I am callable...")

class Phone(Callable):
    def call(self):
        print("Calling...")

class Computer(Callable):
    def call(self):
        print("Starting Discord call...")

class Person(Callable):
    def call(self):
        print("Calling someone in person...")

class Bike:
    def call(self):
        print("Beeeeeeep")

def make_call(device:Callable):
    device.call()
    

make_call(Phone())
make_call(Computer())
make_call(Person())
make_call(157)