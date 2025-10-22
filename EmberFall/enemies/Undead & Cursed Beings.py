import random

# Enemy classes for Undead & Cursed Beings
class Undead_Cursed_Being_enemies():
    def __init__(self, enemy_name):
        self.enemy_name = enemy_name
        
        # Define enemy attributes based on enemy type

        if self.enemy_name == "Restless_Corpse":
            self.health = 80
            self.strength = random.randint(15, 25)
            self.defense = random.randint(20, 40)
            self.dexterity = 20
            self.magic_power = 0
            self.critical = random.randint(5, 15)

        elif self.enemy_name == "Hollow_Shade":
            self.health = 70
            self.strength = random.randint(10, 20)
            self.defense = random.randint(15, 35)
            self.dexterity = 30
            self.magic_power = 0
            self.critical = random.randint(10, 20)

        elif self.enemy_name == "Weeping_Wraith":
            self.health = 60
            self.strength = random.randint(10, 18)
            self.defense = random.randint(10, 30)
            self.dexterity = 35
            self.magic_power = random.randint(15, 25)
            self.critical = random.randint(10, 18)

        elif self.enemy_name == "Gravebound_Knight":
            self.health = 95
            self.strength = random.randint(25, 35)
            self.defense = random.randint(50, 65)
            self.dexterity = 20
            self.magic_power = 0
            self.critical = random.randint(15, 25)

        elif self.enemy_name == "Rotting_Apostle":
            self.health = 75
            self.strength = random.randint(18, 28)
            self.defense = random.randint(25, 45)
            self.dexterity = 25
            self.magic_power = random.randint(10, 20)
            self.critical = random.randint(10, 20)
        
        elif self.enemy_name == "Tomb_Watcher":
            self.health = 85
            self.strength = random.randint(20, 30)
            self.defense = random.randint(35, 55)
            self.dexterity = 25
            self.magic_power = 0
            self.critical = random.randint(12, 22)
        
        elif self.enemy_name == "Soul_Eater":
            self.health = 65
            self.strength = random.randint(15, 22)
            self.defense = random.randint(20, 40)
            self.dexterity = 40
            self.magic_power = random.randint(25, 35)
            self.critical = random.randint(12, 20)
        
        elif self.enemy_name == "Whispering_Skeleton":
            self.health = 55
            self.strength = random.randint(10, 15)
            self.defense = random.randint(15, 30)
            self.dexterity = 45
            self.magic_power = 0
            self.critical = random.randint(5, 12)

        elif self.enemy_name == "Blighted_Revenant":
            self.health = 75
            self.strength = random.randint(18, 28)
            self.defense = random.randint(30, 50)
            self.dexterity = 30
            self.magic_power = random.randint(15, 25)
            self.critical = random.randint(15, 25)

        elif self.enemy_name == "Banshee_of_the_Marsh":
            self.health = 60
            self.strength = random.randint(12, 20)
            self.defense = random.randint(20, 35)
            self.dexterity = 50
            self.magic_power = random.randint(35, 45)
            self.critical = random.randint(10, 20)
