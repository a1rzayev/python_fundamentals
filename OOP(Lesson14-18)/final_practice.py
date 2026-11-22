class GameCharacter:
    def __init__(self, name:str, health:int, damage:int, level:int = 1):
        self.name = name
        self.health = health
        self.max_health = health
        self.damage = damage
        self.level = level

    def attack(self):
        print(f"{self.name} attacks for {self.damage} damage!")

    def take_damage(self, amount: int):
        self.health = max(0, self.health - amount)
        print(f"{self.name} takes {amount} damage! (HP: {self.health}/{self.max_health})")

    def heal(self, amount: int):
        self.health = min(self.max_health, self.health + amount)
        print(f"{self.name} heals for {amount}! (HP: {self.health}/{self.max_health})")

    def show_stats(self):
        print(
            f"Name: {self.name} | Level: {self.level} | "
            f"HP: {self.health}/{self.max_health} | Damage: {self.damage}"
        )



knight = GameCharacter("Knight", health=100, damage=25, level=2)
mage = GameCharacter("Mage", health=80, damage=30, level=2)

knight.show_stats()
mage.show_stats()
print("-" * 45)

knight.attack()
mage.take_damage(20)
mage.heal(10)
print("-" * 45)

knight.show_stats()
mage.show_stats()