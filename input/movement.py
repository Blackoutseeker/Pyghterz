from pygame.key import get_pressed
from state import PlayerState
from .keymap import Keymap
from utils import PlayerAction

speed = 8


class Movement:
    def __init__(self, player_state: PlayerState, is_second_player: bool = False):
        self._player_state: PlayerState = player_state
        self._is_first_player: bool = is_second_player
        self._player_key = Keymap.Player1
        if is_second_player:
            self._player_key = Keymap.Player2
        self._position_x: float = 0
        self._position_y: float = 0

    def get_position_x(self) -> float:
        return self._position_x

    def get_position_y(self) -> float:
        return self._position_y

    def update(self):
        keys = get_pressed()
        is_player_attacking: bool = self._player_state.get_is_attacking()
        if is_player_attacking is False:
            if keys[self._player_key.JUMP.value]:
                self._position_y -= speed
            elif keys[self._player_key.CROUCH.value]:
                self._position_y += speed
            elif keys[self._player_key.BACKWARD.value]:
                self._position_x -= speed
                self._player_state.set_player_action(PlayerAction.MOVE_BACKWARD)
            elif keys[self._player_key.FORWARD.value]:
                self._position_x += speed
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
