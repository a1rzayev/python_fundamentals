# private - accessable and modifyable only in class itself
class Person:
    def __init__(self, name):
        self.__name = name # 2 "_" before attr = private
    

person = Person("Muhammed")
print(person.__name)

# print(person._Person__name) # BAD WAY TO DO IT!!!
# _CLASSNAME__ATTRNAME

