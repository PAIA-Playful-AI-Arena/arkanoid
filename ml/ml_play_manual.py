"""
The template of the main script of the machine learning process
"""
import pygame


class MLPlay:
    def __init__(self, *args, **kwargs):
        """
        Constructor
        """
        self.ball_served = False

    def update(self, scene_info, keyboard=None, *args, **kwargs):
        """
        Generate the command according to the received `scene_info`.
        """
        # Make the caller to invoke `reset()` for the next round.
        if keyboard is None:
            keyboard = []
        if (scene_info["status"] == "GAME_OVER" or
                scene_info["status"] == "GAME_PASS"):
            return "RESET"

        if pygame.K_q in keyboard:
            command = "SERVE_TO_LEFT"
            self.ball_served = True
        elif pygame.K_e in keyboard:
            command = "SERVE_TO_RIGHT"
            self.ball_served = True
        elif pygame.K_LEFT in keyboard or pygame.K_a in keyboard:
            command = "MOVE_LEFT"
        elif pygame.K_RIGHT in keyboard or pygame.K_d in keyboard:
            command = "MOVE_RIGHT"
        else:
            command = "NONE"

        return command

    def reset(self):
        """
        Reset the status
        """
        self.ball_served = False
