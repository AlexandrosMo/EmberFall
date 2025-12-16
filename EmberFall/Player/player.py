import sys
import os

#insert the Classes directory to the Player module path

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Classes.classes import Character


def create_player_interactive():
    """Prompt the user for a name and class and return a Character with a `name` attribute."""
    while True:
        name = input("Enter your character's name: ")
        if name.strip():
            break
        print("Name cannot be empty. Please enter a valid name.")

    print(f"Welcome, {name}! Choose your class from the following options:")
    print(Character.classes)
 
    while True:
        class_type = input("Enter your class: ")
        if class_type in Character.classes:
            break
        print("Invalid class selected. Please choose a valid class.")

    player = Character(class_type, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    # attach the chosen player name
    player.name = name
    
    print(f"You have chosen the {class_type} class. Good luck on your adventure, {name}!")
    print(f"Stats: Strength={player.strength}, Health={player.health}, Defense={player.defense}, Dexterity={player.dexterity}, Mana={player.mana}, Magic Power={player.magic_power}, Critical={player.critical}, Faith={player.faith}, Range={player.range}")

    return player
