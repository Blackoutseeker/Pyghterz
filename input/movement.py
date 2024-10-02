import pygame
from state import PlayerState
from utils import PlayerAction

speed = 8


class Movement:
    def __init__(self, player_state: PlayerState, player_key):
        self._player_state: PlayerState = player_state
        self._player_key = player_key
        self.position_x = 0
        self.position_y = 0

    def update(self):
        keys = pygame.key.get_pressed()
        is_player_attacking: bool = self._player_state.get_is_attacking()
        if is_player_attacking is False:
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

            elif keys[self._player_key.WEAK_PUNCH.value]:
                self._player_state.set_is_attacking(True)
                self._player_state.set_player_action(PlayerAction.WEAK_PUNCH)
            elif keys[self._player_key.MEDIUM_PUNCH.value]:
                self._player_state.set_is_attacking(True)
                self._player_state.set_player_action(PlayerAction.MEDIUM_PUNCH)
            elif keys[self._player_key.HIGH_PUNCH.value]:
                self._player_state.set_is_attacking(True)
                self._player_state.set_player_action(PlayerAction.HIGH_PUNCH)
            elif keys[self._player_key.WEAK_KICK.value]:
                self._player_state.set_is_attacking(True)
                self._player_state.set_player_action(PlayerAction.WEAK_KICK)
            elif keys[self._player_key.MEDIUM_KICK.value]:
                self._player_state.set_is_attacking(True)
                self._player_state.set_player_action(PlayerAction.MEDIUM_KICK)
            elif keys[self._player_key.HIGH_KICK.value]:
                self._player_state.set_is_attacking(True)
                self._player_state.set_player_action(PlayerAction.HIGH_KICK)
            else:
                self._player_state.set_player_action(PlayerAction.IDLE)
