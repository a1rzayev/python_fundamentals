class GameCharacter:

    def __init__(self, name, health, damage, level):
        self.name = name
        self.health = health
        self.damage = damage
        self.level = level

    def attack(self):
        print("f{self.name} attacks and delas {self.damage} damage!")

    def take_damage(self, amount):
        self.health -= amount
        if(self.health < 0):
            self.health = 0
        print(f"{self.name} has {self.health} HP left")

    def show_statistics(self):
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Damage: {self.damage}")
        print(f"Level: {self.level}")


warrior = GameCharacter("Warrior", 100, 25, 5)
mage = GameCharacter("Mage", 80, 40, 3)

warrior.attack()
mage.take_damage(25)

mage.attack()
warrior.take_damage(40)

warrior.show_statistics()
mage.show_statistics()