import random

#define Nature Tainted enemy attributes

class Nature_Tainted_enemies():
    def __init__(self, enemy_name):
        self.enemy_name = enemy_name
        
        # Define enemy attributes based on enemy type

        if self.enemy_name == "Thorned_Dryad":
            self.health = 75
            self.strength = random.randint(10, 20)
            self.defense = random.randint(30, 45)
            self.dexterity = 40
            self.magic_power = random.randint(20, 30)
            self.critical = random.randint(10, 20)

        elif self.enemy_name == "Blightroot_Guardian":
            self.health = 100
            self.strength = random.randint(20, 30)
            self.defense = random.randint(45, 60)
            self.dexterity = 20
            self.magic_power = random.randint(15, 25)
            self.critical = random.randint(12, 22)

        elif self.enemy_name == "Fungal_Beast":
            self.health = 85
            self.strength = random.randint(15, 25)
            self.defense = random.randint(35, 50)
            self.dexterity = 25
            self.magic_power = random.randint(10, 20)
            self.critical = random.randint(10, 18)

        elif self.enemy_name == "Mossbound_Stalker":
            self.health = 70
            self.strength = random.randint(15, 25)
            self.defense = random.randint(25, 40)
            self.dexterity = 45
            self.magic_power = random.randint(15, 25)
            self.critical = random.randint(15, 25)

        elif self.enemy_name == "Corrosive_Slug":
            self.health = 60
            self.strength = random.randint(5, 15)
            self.defense = random.randint(15, 30)
            self.dexterity = 20
            self.magic_power = random.randint(25, 35)
            self.critical = random.randint(5, 12)

        elif self.enemy_name == "Hollow_Treant":
            self.health = 110
            self.strength = random.randint(25, 35)
            self.defense = random.randint(50, 65)
            self.dexterity = 15
            self.magic_power = random.randint(10, 20)
            self.critical = random.randint(10, 20)
