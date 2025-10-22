
#define Main Boss attributes

class Main_Bosses():
    def __init__(self, boss_name):
        self.boss_name = boss_name

        #δefine boss attributes based on boss type
 
        if self.boss_name == "Abyssar: The Shadow of Emberfall":
            self.health = 650
            self.strength = 170
            self.defense = 220
            self.dexterity = 90
            self.magic_power = 80
            self.critical = 75

        elif self.boss_name == "Draemor: The Dread Warden":
            self.health = 600
            self.strength = 200
            self.defense = 200
            self.dexterity = 80
            self.magic_power = 70
            self.critical = 70
    
        elif self.boss_name == "Vorynth: The Void Serpent":
            self.health = 580
            self.strength = 180
            self.defense = 170
            self.dexterity = 100
            self.magic_power = 100
            self.critical = 75

        elif self.boss_name == "Malrath: The Corruptor":
            self.health = 620
            self.strength = 190
            self.defense = 210
            self.dexterity = 85
            self.magic_power = 90
            self.critical = 80

        elif self.boss_name == "Ignivar: The Infernal Colossus":
            self.health = 700
            self.strength = 220
            self.defense = 230
            self.dexterity = 70
            self.magic_power = 60
            self.critical = 60

        elif self.boss_name == "Noctyra: The Nightmare Wraith":
            self.health = 580
            self.strength = 150
            self.defense = 180
            self.dexterity = 120
            self.magic_power = 110
            self.critical = 85

        elif self.boss_name == "Zerathiel: The Emberfall Guardian":
            self.health = 650
            self.strength = 210
            self.defense = 240
            self.dexterity = 75
            self.magic_power = 50
            self.critical = 65
