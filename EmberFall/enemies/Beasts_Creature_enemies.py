import random

# Enemy classes for Beasts & Creature type enemies
class Beasts_Creature_enemies():
    def __init__(self, enemy_name):
        self.enemy_name = enemy_name

        # Define enemy attributes based on enemy type

        if self.enemy_name == "Carrion_Wolf":
            self.health = 70
            self.strength = random.randint(15, 25)
            self.defense = random.randint(25, 40)
            self.dexterity = 40
            self.magic_power = 0
            self.critical = random.randint(15, 25)

        elif self.enemy_name == "Rotfang_Spider":
            self.health = 60
            self.strength = random.randint(10, 20)
            self.defense = random.randint(20, 35)
            self.dexterity = 50
            self.magic_power = 0
            self.critical = random.randint(10, 20)

        elif self.enemy_name == "Bone_Serpent":
            self.health = 80
            self.strength = random.randint(20, 30)
            self.defense = random.randint(35, 55)
            self.dexterity = 30
            self.magic_power = 0
            self.critical = random.randint(20, 30)

        elif self.enemy_name == "Ash_Hound":
            self.health = 75
            self.strength = random.randint(20, 28)
            self.defense = random.randint(35, 50)
            self.dexterity = 35
            self.magic_power = 0
            self.critical = random.randint(15, 25)

        elif self.enemy_name == "Mire_Leech":
            self.health = 55
            self.strength = random.randint(10, 18)
            self.defense = random.randint(20, 30)
            self.dexterity = 45
            self.magic_power = 0
            self.critical = random.randint(10, 18)
        
        elif self.enemy_name == "Ember_Rat":
            self.health = 40
            self.strength = random.randint(5, 12)
            self.defense = random.randint(10, 20)
            self.dexterity = 50
            self.magic_power = 0
            self.critical = random.randint(5, 12)

        elif self.enemy_name == "Feral_Stalker":
            self.health = 85
            self.strength = random.randint(25, 35)
            self.defense = random.randint(45, 60)
            self.dexterity = 30
            self.magic_power = 0
            self.critical = random.randint(20, 30)
        
        elif self.enemy_name == "Abyssal_Boar":
            self.health = 90
            self.strength = random.randint(30, 40)
            self.defense = random.randint(50, 65)
            self.dexterity = 25
            self.magic_power = 0
            self.critical = random.randint(15, 25)
        
        elif self.enemy_name == "Dire_Vulture":
            self.health = 65
            self.strength = random.randint(15, 25)
            self.defense = random.randint(25, 40)
            self.dexterity = 55
            self.magic_power = 0
            self.critical = random.randint(20, 30)

        elif self.enemy_name == "Cracked_Golem":
            self.health = 100
            self.strength = random.randint(35, 45)
            self.defense = random.randint(60, 80)
            self.dexterity = 10
            self.magic_power = 0
            self.critical = random.randint(5, 15)
