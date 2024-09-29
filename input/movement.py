import pygame
from state import PlayerState
from .keymap import Keymap
from utils import PlayerAction

speed = 8


class Movement:
    def __init__(self, player_state: PlayerState):
        self._player_state: PlayerState = player_state
        self._player_key = Keymap.Player1
        self.position_x = 0
        self.position_y = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[self._player_key.JUMP.value]:
            self.position_y -= speed
        elif keys[self._player_key.CROUCH.value]:
            self.position_y += speed
        elif keys[self._player_key.BACKWARD.value]:
            self.position_x -= speed
            self._player_state.set_player_action(PlayerAction.MOVE_BACKWARD)
        elif keys[self._player_key.FORWARD.value]:
            self.position_x += speed
            self._player_state.set_player_action(PlayerAction.MOVE_FORWARD)
        else:
            self._player_state.set_player_action(PlayerAction.IDLE)
