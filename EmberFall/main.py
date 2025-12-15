import sys
import os
import yaml

from Player.player import create_player_interactive

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

with open('EmberFall/data/intro.yml' , 'r') as f:
            intro_data = yaml.safe_load(f)
          

class EmberFallGame():
    def __init__(self):
        options = input("WELCOME TO EMBERFALL \n 1. Start New Game \n 2. Load Game \n Choose an option: ")
        if options == "1":
            self.start_new_game()
            print(intro_data)
        elif options == "2":
            self.load_game()
    def start_new_game(self):
        # create player interactively (prompts for name/class)
        self.player = create_player_interactive()
        print(f"Welcome, {self.player.name}, to the world of EmberFall!")
        world_map.start_adventure(self.player)

    def load_game(self):
        self.player = save_system.load_game()
        if self.player:
            print(f"Welcome back, {self.player.name}!")
            world_map.start_adventure(self.player)
        else:
            print("No saved game found. Starting a new game.")
            self.start_new_game()


EmberFallGame()