# public - accessable and modifyable only in inheritenced classes
class Person:
    def __init__(self, name):
        self._name = name # 1 "_" before attr = protected

person = Person("Vali")

print(person._name)