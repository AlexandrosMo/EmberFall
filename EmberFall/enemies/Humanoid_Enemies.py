import random

# Enemy classes for Humanoid type enemies
class Humanoid_Enemies():
    def __init__(self, enemy_name):
        self.enemy_name = enemy_name

        # Define enemy attributes based on enemy type

        if self.enemy_name == "Hollow_Knight":
            self.health = 80
            self.strength = random.randint(15, 25)
            self.defense = random.randint(40, 55)
            self.dexterity = 20
            self.magic_power = 5
            self.critical = random.randint(10, 20)

        elif self.enemy_name == "Forsaken_Soldier":
            self.health = 70
            self.strength = random.randint(12, 22)
            self.defense = random.randint(30, 50)
            self.dexterity = 15
            self.magic_power = 5
            self.critical = random.randint(5, 15)

        elif self.enemy_name == "Mad_Peasant":
            self.health = 50
            self.strength = random.randint(5, 15)
            self.defense = random.randint(20, 35)
            self.dexterity = 25
            self.magic_power = 0
            self.critical = random.randint(5, 10)

        elif self.enemy_name == "Corrupted_Acolyte":
            self.health = 60
            self.strength = random.randint(10, 18)
            self.defense = random.randint(25, 40)
            self.dexterity = 20
            self.magic_power = random.randint(25, 35)
            self.critical = random.randint(5, 15)

        elif self.enemy_name == "Ashbound_Mercenary":
            self.health = 85
            self.strength = random.randint(20, 30)
            self.defense = random.randint(50, 65)
            self.dexterity = 15
            self.magic_power = 5
            self.critical = random.randint(15, 25)

        elif self.enemy_name == "Wretched_Pilgrim":
            self.health = 45
            self.strength = random.randint(5, 12)
            self.defense = random.randint(10, 25)
            self.dexterity = 15
            self.magic_power = 0
            self.critical = random.randint(5, 10)

        elif self.enemy_name == "Blighted_Monk":
            self.health = 60
            self.strength = random.randint(10, 18)
            self.defense = random.randint(30, 50)
            self.dexterity = 15
            self.magic_power = random.randint(25, 35)
            self.critical = random.randint(10, 18)

        elif self.enemy_name == "Faithless_Sentinel":
            self.health = 70
            self.strength = random.randint(15, 25)
            self.defense = random.randint(35, 55)
            self.dexterity = 15
            self.magic_power = 5
            self.critical = random.randint(15, 20)

        elif self.enemy_name == "Burned_Crusader":
            self.health = 90
            self.strength = random.randint(25, 35)
            self.defense = random.randint(50, 70)
            self.dexterity = 15
            self.magic_power = 5
            self.critical = random.randint(20, 30)

        elif self.enemy_name == "Bloodless_Priest":
            self.health = 50
            self.strength = random.randint(5, 12)
            self.defense = random.randint(20, 40)
            self.dexterity = 25
            self.magic_power = random.randint(55, 65)
            self.critical = random.randint(15, 30)
