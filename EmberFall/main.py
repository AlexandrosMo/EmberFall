import sys
import os
import yaml
import time

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
            start = input("Press Enter to begin your adventure...")
            if start == "":
                print(f"Welcome, {self.player.name}, to the world of EmberFall!")
                for c in intro_data:
                        sys.stdout.write(c)
                        sys.stdout.flush()
                        time.sleep(0.05)
                        if c == ".":
                            sys.stdout.write(c)
                            sys.stdout.flush()
                            time.sleep(0.05)
                            enter = input("\npress enter to continue or s to skip...")
                            print (enter)
                            if enter == press("s"):
                                break
                print(c)

            else:
                for start in start:
                    if start != "enter":
                        print(input("press Enter Bro.."))
                        if start != "enter":
                            print(input("if you dont press enter you cant play.."))
                            if start != "enter":
                                print(input("if you press any other key you are gay.."))
                                if start != "enter":
                                    print(input("just press enter smh.."))
                                    if start != "enter":
                                        print("Nevermind, Good Luck Stupid!..")

                    print(f"Welcome, {self.player.name}, to the world of EmberFall!")

        else:
            options == "2"
            self.load_game()

    def load_game(self):
        self.player = save_system.load_game()
        if self.player:
            print(f"Welcome back, {self.player.name}!")
        else:
            print("No saved game found. Starting a new game.")
            self.start_new_game()


EmberFallGame() 