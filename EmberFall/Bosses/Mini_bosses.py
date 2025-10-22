class Mini_Bosses():

    #define Mini Boss attributes
    def __init__(self, boss_name):
        self.boss_name = boss_name

        #define Mini Boss attributes based on boss type

        if self.boss_name == "Gorath: The Ashbound Sentinel":
            self.health = 350
            self.strength = 90
            self.defense = 90
            self.dexterity = 50
            self.magic_power = 15
            self.critical = 20

        elif self.boss_name == "Sylvara: The Venom Queen":
            self.health = 300
            self.strength = 70
            self.defense = 50
            self.dexterity = 75
            self.magic_power = 40
            self.critical = 25

        elif self.boss_name == "Korvath: The Forsaken General":
            self.health = 320
            self.strength = 75
            self.defense = 80
            self.dexterity = 55
            self.magic_power = 15
            self.critical = 20

        elif self.boss_name == "Mireclaw: The Swamp Horror":
            self.health = 360
            self.strength = 80
            self.defense = 90
            self.dexterity = 40
            self.magic_power = 10
            self.critical = 15

        elif self.boss_name == "Thrynos: The Sky Reaper":
            self.health = 280
            self.strength = 65
            self.defense = 60
            self.dexterity = 90
            self.magic_power = 20
            self.critical = 25

        elif self.boss_name == "Ashveil: The Cursed Monk":
            self.health = 300
            self.strength = 70
            self.defense = 70
            self.dexterity = 50
            self.magic_power = 50
            self.critical = 20

        elif self.boss_name == "Bonehowl: The Crypt Guardian":
            self.health = 340
            self.strength = 75
            self.defense = 100
            self.dexterity = 35
            self.magic_power = 10
            self.critical = 15

        elif self.boss_name == "Frostmaw: The Winter Fiend":
            self.health = 310
            self.strength = 70
            self.defense = 70
            self.dexterity = 45
            self.magic_power = 50
            self.critical = 20

        elif self.boss_name == "Emberling: The Lava Spawn":
            self.health = 300
            self.strength = 70
            self.defense = 60
            self.dexterity = 70
            self.magic_power = 30
            self.critical = 25

        elif self.boss_name == "Shadefang: The Night Stalker":
            self.health = 250
            self.strength = 60
            self.defense = 50
            self.dexterity = 90
            self.magic_power = 15
            self.critical = 30
