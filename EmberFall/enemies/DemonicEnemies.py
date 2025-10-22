import random

#define Demonic enemy attributes

class DemonicEnemies():
    def __init__(self,Demonic_name):
        self.Demonic_name = Demonic_name

    #define enemy attributes based on enemy type
    
        if self.Demonic_name == "Lesser Demon":
            self.health = 80
            self.strength = random.randint(15, 25)
            self.defense = random.randint(25, 40)
            self.dexterity = 25
            self.magic_power = random.randint(15, 25)
            self.critical = random.randint(10, 20)

        elif self.Demonic_name == "Flamebound Imp":
            self.health = 70
            self.strength = random.randint(12, 20)
            self.defense = random.randint(20, 35)
            self.dexterity = 30
            self.magic_power = random.randint(20, 30)
            self.critical = random.randint(10, 18)

        elif self.Demonic_name == "Abyss Spawn":
            self.health = 100
            self.strength = random.randint(25, 35)
            self.defense = random.randint(35, 50)
            self.dexterity = 20
            self.magic_power = random.randint(25, 35)
            self.critical = random.randint(15, 25)

        elif self.Demonic_name == "Voidling":
            self.health = 85
            self.strength = random.randint(18, 28)
            self.defense = random.randint(25, 40)
            self.dexterity = 35
            self.magic_power = random.randint(20, 30)
            self.critical = random.randint(12, 22)
        
        elif self.Demonic_name == "Infernal Hound":
            self.health = 90
            self.strength = random.randint(22, 32)
            self.defense = random.randint(30, 45)
            self.dexterity = 30
            self.magic_power = random.randint(20, 30)
            self.critical = random.randint(15, 25)

        elif self.Demonic_name == "Corrupted Cherub":
            self.health = 65
            self.strength = random.randint(10, 18)
            self.defense = random.randint(20, 35)
            self.dexterity = 40
            self.magic_power = random.randint(25, 35)
            self.critical = random.randint(10, 18)

        elif self.Demonic_name == "Shadow Fiend":
            self.health = 100
            self.strength = random.randint(28, 38)
            self.defense = random.randint(40, 55)
            self.dexterity = 25
            self.magic_power = random.randint(30, 40)
            self.critical = random.randint(18, 28)
        
        elif self.Demonic_name == "Bloodflame Thrall":
            self.health = 110
            self.strength = random.randint(30, 40)
            self.defense = random.randint(45, 60)
            self.dexterity = 20
            self.magic_power = random.randint(35, 45)
            self.critical = random.randint(20, 30)

        elif self.Demonic_name == "Pit Serpent":
            self.health = 120
            self.strength = random.randint(35, 45)
            self.defense = random.randint(50, 65)
            self.dexterity = 15
            self.magic_power = random.randint(40, 50)
            self.critical = random.randint(22, 32)

        elif self.Demonic_name == "Emberborn Demon":
            self.health = 130
            self.strength = random.randint(40, 50)
            self.defense = random.randint(55, 70)
            self.dexterity = 10
            self.magic_power = random.randint(45, 55)
            self.critical = random.randint(25, 35)
