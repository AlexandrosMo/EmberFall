import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Player.player import Player
from Bosses import Main_Bosses
from Bosses import Mini_Bosses
from enemies.enemy import Enemy

class LevelUp():
    player_level = 1
    def __init__(self, player):
        self.player = player

    def level_up(self):
        self.player.level += 1
        self.player.strength += 5
        self.player.health += 10
        self.player.defense += 3
        self.player.dexterity += 4
        self.player.mana += 6
        self.player.magic_power += 4
        self.player.critical += 2
        self.player.faith += 2
        self.player.range += 1
        print(f"Congratulations! You've reached level {self.player.level}!")
        print(f"New stats - Strength: {self.player.strength}, Health: {self.player.health}, Defense: {self.player.defense}, Dexterity: {self.player.dexterity}, Mana: {self.player.mana}, Magic Power: {self.player.magic_power}, Critical: {self.player.critical}, Faith: {self.player.faith}, Range: {self.player.range}")

