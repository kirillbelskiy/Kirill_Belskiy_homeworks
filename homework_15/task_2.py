class Weapon:
    def __init__(self, name, damage, durability):
        self.name = name
        self.damage = damage
        self.durability = durability

class Armor:
    def __init__(self, name, protection, durability):
        self.name = name
        self.protection = protection
        self.durability = durability

class Robot:
    def __init__(self, name):
        self.name = name
        self.weapons = []
        self.armors = []

    def add_weapon(self, weapon):
        self.weapons.append(weapon)

    def add_armor(self, armor):
        self.armors.append(armor)

    def print_arsenal(self):
        print(f"Робот {self.name} вооружен следующими предметами:")
        for weapon in self.weapons:
            print(f"Оружие: {weapon.name}, Урон: {weapon.damage}, Прочность: {weapon.durability}")
        for armor in self.armors:
            print(f"Броня: {armor.name}, Защита: {armor.protection}, Прочность: {armor.durability}")

sword = Weapon("Меч", 50, 100)
gun = Weapon("Автомат", 100, 200)
armor = Armor("Броня", 50, 100)
helmet = Armor("Шлем", 30, 80)

robot = input("Введите имя робота: ")
robot = Robot(robot)

robot.add_weapon(sword)
robot.add_weapon(gun)
robot.add_armor(armor)
robot.add_armor(helmet)

robot.print_arsenal()
