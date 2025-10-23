import sys
import os

#insert the Classes directory to the Player module path

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Classes.classes import Character

name = input("Enter your character's name: ")

print(f"Welcome, {name}! Choose your class from the following options:")
print(Character.classes)

class_type = input("Enter your class: ")

#validate class selection
#if the class is valid it prints the Character stats

if class_type not in Character.classes:
    print("Invalid class selected. Please choose a valid class.")
else:
    player = Character(class_type, 0, 0, 0, "Basic Weapon", 0, 0, 0, 0, 0)
    print(f"You have chosen the {class_type} class. Good luck on your adventure, {name}!")
    print(f"Stats: Strength={player.strength}, Health={player.health}, Defense={player.defense}, Dexterity={player.dexterity}, Mana={player.mana}, Magic Power={player.magic_power}, Critical={player.critical}, Faith={player.faith}, Range={player.range}")
