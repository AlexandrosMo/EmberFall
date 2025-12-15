import sys
import os
import yaml

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Player.player import create_player_interactive

# open intro relative to this file so imports or different working directories don't break it
intro_path = os.path.join(os.path.dirname(__file__), 'data', 'intro.yml')
with open(intro_path, 'r') as f:
    intro_data = yaml.safe_load(f)
          

class EmberFallGame():
    def __init__(self):
        options = input("WELCOME TO EMBERFALL \n 1. Start New Game \n 2. Load Game \n Choose an option: ")
        if options == "1":
            
        # create player interactively (prompts for name/class)
            self.player = create_player_interactive()
            print(f"Welcome, {self.player.name}, to the world of EmberFall!")
            start= input("Press any key to begin your adventure...")
            if start == "":
                print(intro_data)
            elif start != "":
                print(input("press Enter Bro.."))
                if start != "":
                    print(input("if you dont press enter you cant play.."))
                    if start != "":
                        print(input("if you press any other key you are gay.."))
                        if start != "":
                            print(input("just press enter smh.."))
                            if start != "":
                                print("Nevermind, Good Luck Stupid!..")

            self.start_new_game()
           
        elif options == "2":
            self.load_game()
         

    def load_game(self):
        self.player = save_system.load_game()
        if self.player:
            print(f"Welcome back, {self.player.name}!")
        else:
            print("No saved game found. Starting a new game.")
            self.start_new_game()


EmberFallGame() 