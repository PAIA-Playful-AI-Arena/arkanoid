from os import path

ASSET_DIR = path.join(path.dirname(__file__), "../asset")
ASSET_LEVEL_DIR = path.join(path.dirname(__file__), "../asset/level_data")
ASSET_IMAGE_DIR = path.join(path.dirname(__file__), "../asset/img")

BG_PATH = path.join(ASSET_IMAGE_DIR, "background.png")
BRICK_PATH = path.join(ASSET_IMAGE_DIR, "brick.png")
HARD_BRICK_PATH = path.join(ASSET_IMAGE_DIR, "hard_brick.png")
BOARD_PATH = path.join(ASSET_IMAGE_DIR, "board.png")
BALL_PATH = path.join(ASSET_IMAGE_DIR, "ball.png")

ASSET_IMG_URL = "https://raw.githubusercontent.com/PAIA-Playful-AI-Arena/arkanoid/main/asset/img/"
BG_URL = ASSET_IMG_URL + "background.png"

BRICK_URL = ASSET_IMG_URL + "brick.png"
HARD_BRICK_URL = ASSET_IMG_URL + "hard_brick.png"
BOARD_URL = ASSET_IMG_URL + "board.png"
BALL_URL = ASSET_IMG_URL + "ball.png"
