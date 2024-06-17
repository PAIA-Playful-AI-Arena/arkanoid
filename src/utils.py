from functools import lru_cache

from games.arkanoid.src.env import BG_LEFT_WIDTH


def shift_left_with_bg_width(pos: tuple) -> tuple:
    return (pos[0] - BG_LEFT_WIDTH, pos[1])

@lru_cache
def shift_left_with_bg_width_by_lru(pos: tuple) -> tuple:
    return (pos[0] - BG_LEFT_WIDTH, pos[1])
