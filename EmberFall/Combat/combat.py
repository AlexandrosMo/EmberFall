import sys
import os

#insert the Classes directory to the Player module path

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Player.player import Player