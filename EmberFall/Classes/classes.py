
class Character():
     classes = ["Warrior", "Mage", "Rogue", "Ranger", "Paladin", "Occultist", "Berserker"]
     def __init__(self,class_type,strength, health, defense,dexterity, mana, magic_power, critical, faith, range):
        
        self.class_type = class_type
        self.strength = strength
        self.health = health
        self.defense = defense
        self.dexterity = dexterity
        self.mana = mana
        self.magic_power = magic_power
        self.critical = critical
        self.faith = faith
        self.range = range

        if class_type == "Warrior":
            self.strength = 85
            self.health = 100
            self.defense = 80
            self.dexterity = 50
            self.mana = 30
            self.magic_power = 5
            self.critical = 20
            self.faith = 0
            self.range = 0


        elif class_type == "Mage":
            self.strength = 15
            self.health = 60
            self.defense = 40
            self.dexterity = 45
            self.mana = 90
            self.magic_power = 50
            self.critical = 10
            self.faith = 0
            self.range = 0

        elif class_type == "Rogue":
            self.strength = 60
            self.health = 70
            self.defense = 50
            self.dexterity = 85
            self.mana = 25
            self.magic_power = 10
            self.critical = 30
            self.faith = 0
            self.range = 0

        elif class_type == "Ranger":
            self.strength = 65
            self.health = 75
            self.defense = 60
            self.dexterity = 70
            self.mana = 30
            self.magic_power = 15
            self.critical = 25
            self.faith = 0
            self.range = 10

        elif class_type == "Paladin":
            self.strength = 75
            self.health = 90
            self.defense = 85
            self.dexterity = 40
            self.mana = 50
            self.magic_power = 25
            self.critical = 15
            self.faith = 30
            self.range = 0

        elif class_type == "Occultist":
            self.strength = 40
            self.health = 65
            self.defense = 45
            self.dexterity = 50
            self.mana = 95
            self.magic_power = 60
            self.critical = 15
            self.faith = 20
            self.range = 0

        elif class_type == "Berserker":
            self.strength = 95
            self.health = 110
            self.defense = 70
            self.dexterity = 55
            self.mana = 20
            self.magic_power = 5
            self.critical = 25
            self.faith = 0
            self.range = 0
       


      



