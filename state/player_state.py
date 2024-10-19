from utils import PlayerAction
from typing import List
from pygame.time import get_ticks


class PlayerState:
    def __init__(self):
        self._player_action: PlayerAction = PlayerAction.IDLE
        self._position_x: float = 0
        self._position_y: float = 0
        self._is_attacking: bool = False
        self._is_facing_right: bool = True
        self._sprite_index: int = 0
        self._animation_update_time: float = 0

    def get_player_action(self) -> PlayerAction:
        return self._player_action

    def set_player_action(self, player_action: PlayerAction):
        self._player_action = player_action

    def get_player_position(self) -> List[float]:
        return [self._position_x, self._position_y]

    def set_player_position_x(self, position_x: float):
        self._position_x = position_x

    def set_player_position_y(self, position_y: float):
        self._position_y = position_y

    def get_is_attacking(self) -> bool:
        return self._is_attacking

    def set_is_attacking(self, is_attacking: bool):
        self._is_attacking = is_attacking

    def get_is_facing_right(self) -> bool:
        return self._is_facing_right

    def set_is_facing_right(self, is_facing_right: bool):
        self._is_facing_right = is_facing_right

    def get_sprite_index(self) -> int:
        return self._sprite_index

    def set_sprite_index(self, sprite_index: int):
        self._sprite_index = sprite_index

    def get_animation_update_time(self) -> float:
        return self._animation_update_time

    def set_animation_update_time(self, animation_update_time: float):
        self._animation_update_time = animation_update_time

    def reset_animation_attributes(self):
        self._sprite_index = 0
        self._animation_update_time = get_ticks()
