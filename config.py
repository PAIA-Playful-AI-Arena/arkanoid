import sys
from os import path
sys.path.append(path.dirname(__file__))

from src.game import Arkanoid

GAME_SETUP = {
    "game": Arkanoid
}
