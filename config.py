import sys
from os import path
sys.path.append(path.dirname(__file__))
# TODO smaller bg

from src.game import Arkanoid

GAME_SETUP = {
    "game": Arkanoid,
    # "dynamic_ml_clients":True
}
