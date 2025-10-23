import sys
import os
import random

#insert the Classes directory to the Player module path

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Player.player import Player
from enemies.enemy import Enemy
from bosses.boss import Boss
from bosses.mini_bosses import MiniBoss

def start_combat(player, enemy):
    print(f"Throw the Woods you hear something moving...")
    print(f"you look closer and you see a figure behind the trees, you look closer and then you see a {enemy.name}!")
    print(f"What will you do?")
    print("1. Attack")
    print("2. Run Away")
    action = input("Choose your action (1 or 2): ")
    if action == "1":
        print (f"You draw your weapon and prepare to fight the {enemy.name}!")
        while player.health > 0 and enemy.health > 0:
            player_attack = random.randint(0, player.strength) - enemy.defense
            enemy_attack = random.randint(0, enemy.strength) - player.defense
            if player_attack <= 0:
                print (f"Your attack missed the {enemy.name}!")
            elif player_attack > 0:
                enemy.health -= player_attack
                print (f"You dealt {player_attack} damage to the {enemy.name}. It has {enemy.health} health left.")
            if enemy.health <= 0:
                print (f"You have defeated the {enemy.name}!")
                print (f"Enemy dropped {drops}", "you gained {Exp} experience points!")
                break
