from utils import Character, PlayerAction, MoveSetStats, Config
from typing import List
from pygame.time import get_ticks


class PlayerState:
    def __init__(self, character: Character, is_second_player: bool = False):
        self._character: Character = character
        self._is_second_player: bool = is_second_player
        self._player_action: PlayerAction = PlayerAction.IDLE
        self._position_x, self._position_y = MoveSetStats(character, is_second_player).get_initial_position()
        self._initial_position_x, self._initial_position_y = self._position_x, self._position_y
        self._scale: float = MoveSetStats(character).get_character_scale()
        self._scaled_body_rectangle_area: List[float] = MoveSetStats(character).get_body_rectangle_area_scaled()
        self._is_attacking: bool = False
        self._is_facing_right: bool = True
        self._is_blocking: bool = False
        self._is_getting_weak_hit: bool = False
        self._is_getting_medium_hit: bool = False
        self._is_getting_high_hit: bool = False
        self._sprite_index: int = 0
        self._animation_update_time: float = 0
        self._movements_speed: dict = MoveSetStats(character).get_movements_speed()
        self._attacks_damage: dict = MoveSetStats(character).get_attacks_damage()
        self._health: int = Config.MAXIMUM_PLAYER_HEALTH.value
        self._win: bool = False
        self._lose: bool = False

    def get_character(self) -> Character:
        return self._character

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

    def get_scale(self) -> float:
        return self._scale

    def get_body_rectangle_area_scaled(self) -> List[float]:
        return self._scaled_body_rectangle_area

    def get_is_attacking(self) -> bool:
        return self._is_attacking

    def set_is_attacking(self, is_attacking: bool):
        self._is_attacking = is_attacking

    def get_is_facing_right(self) -> bool:
        return self._is_facing_right

    def set_is_facing_right(self, is_facing_right: bool):
        self._is_facing_right = is_facing_right

    def get_is_blocking(self) -> bool:
        return self._is_blocking

    def set_is_blocking(self, is_blocking: bool):
        self._is_blocking = is_blocking

    def get_is_getting_weak_hit(self) -> bool:
        return self._is_getting_weak_hit

    def set_is_getting_weak_hit(self, is_getting_weak_hit: bool):
        self._is_getting_weak_hit = is_getting_weak_hit

    def get_is_getting_medium_hit(self) -> bool:
        return self._is_getting_medium_hit

    def set_is_getting_medium_hit(self, is_getting_medium_hit: bool):
        self._is_getting_medium_hit = is_getting_medium_hit

    def get_is_getting_high_hit(self) -> bool:
        return self._is_getting_high_hit

    def set_is_getting_high_hit(self, is_getting_strong_hit: bool):
        self._is_getting_high_hit = is_getting_strong_hit

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

    def get_movements_speed(self) -> dict:
        return self._movements_speed

    def get_attacks_damage(self) -> dict:
        return self._attacks_damage

    def get_health(self) -> float:
        return self._health

    def increase_health(self, value: float):
        self._health += value

    def decrease_health(self, value: float):
        self._health -= value

    def get_win(self) -> bool:
        return self._win

    def set_win(self, win: bool):
        self._win = win

    def get_lose(self) -> bool:
        return self._lose

    def set_lose(self, lose: bool):
        self._lose = lose

    def get_initial_position(self) -> List[int]:
        return [self._position_x, self._position_y]

    def reset_all_states(self):
        self._player_action: PlayerAction = PlayerAction.IDLE
        self._position_x, self._position_y = self._initial_position_x, self._initial_position_y
        self._is_attacking: bool = False
        self._is_facing_right: bool = True
        self._is_blocking: bool = False
        self._is_getting_weak_hit: bool = False
        self._is_getting_medium_hit: bool = False
        self._is_getting_high_hit: bool = False
        self._sprite_index: int = 0
        self._animation_update_time: float = 0
        self._health: int = Config.MAXIMUM_PLAYER_HEALTH.value
        self._win: bool = False
        self._lose: bool = False
