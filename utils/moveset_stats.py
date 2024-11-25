from enum import Enum
from .character import Character
from typing import List


class MovementSpeed(Enum):
    MOVE_FORWARD = 8
    MOVE_BACKWARD = 6


class AttackDamage(Enum):
    WEAK_PUNCH = 20
    MEDIUM_PUNCH = 26
    HIGH_PUNCH = 30
    WEAK_KICK = 15
    MEDIUM_KICK = 22
    HIGH_KICK = 32


class MoveSetStats:
    def __init__(self, character: Character, is_second_player: bool = False):
        self._character = character
        self._movements_speed: dict = self._get_character_movements_speed(character)
        self._attacks_damage: dict = self._get_character_attacks_damage(character)
        self._initial_position_x, self._initial_position_y = self._get_initial_position(character, is_second_player)
        self._character_scale: float = self._get_character_scale(character)
        self._body_rectangle_area: List[float] = self._get_body_rectangle_area(character)

    def get_movements_speed(self) -> dict:
        return self._movements_speed

    def get_attacks_damage(self) -> dict:
        return self._attacks_damage

    def get_initial_position(self) -> List[int]:
        return [self._initial_position_x, self._initial_position_y]

    def get_character_scale(self) -> float:
        return self._character_scale

    def get_body_rectangle_area_scaled(self) -> [float]:
        body_rectangle_width, body_rectangle_height = self._body_rectangle_area
        scaled_body_rectangle_width: float = body_rectangle_width * self._character_scale
        scaled_body_rectangle_height: float = body_rectangle_height * self._character_scale
        return [scaled_body_rectangle_width, scaled_body_rectangle_height]

    @staticmethod
    def _get_character_movements_speed(character: Character) -> dict:
        movements_speed: dict = {}

        if character == Character.RYU:
            for movement in MovementSpeed:
                movement_speed: int = movement.value

                if movement == MovementSpeed.MOVE_FORWARD:
                    movement_speed = 8
                elif movement == MovementSpeed.MOVE_BACKWARD:
                    movement_speed = 6

                movements_speed[movement.name] = movement_speed

        return movements_speed

    @staticmethod
    def _get_character_attacks_damage(character: Character) -> dict:
        attacks_damage: dict = {}

        if character == Character.RYU:
            for attack in AttackDamage:
                attack_damage: int = attack.value

                if attack == AttackDamage.WEAK_PUNCH:
                    attack_damage = 20
                elif attack == AttackDamage.MEDIUM_PUNCH:
                    attack_damage = 26
                elif attack == AttackDamage.HIGH_PUNCH:
                    attack_damage = 26
                elif attack == AttackDamage.WEAK_KICK:
                    attack_damage = 18
                elif attack == AttackDamage.MEDIUM_KICK:
                    attack_damage = 30
                elif attack == AttackDamage.HIGH_KICK:
                    attack_damage = 30

                attacks_damage[attack.name] = attack_damage

        return attacks_damage

    @staticmethod
    def _get_initial_position(character: Character, is_second_player: bool) -> List[int]:
        initial_position_x, initial_position_y = 0, 0

        if character == Character.RYU:
            initial_position_x, initial_position_y = 80, 180
            if is_second_player:
                initial_position_x, initial_position_y = 330, 180

        return [initial_position_x, initial_position_y]

    @staticmethod
    def _get_character_scale(character: Character) -> float:
        scale = 1

        if character == Character.RYU:
            scale = 2.4

        return scale

    @staticmethod
    def _get_body_rectangle_area(character: Character) -> List[float]:
        body_rectangle_width, body_rectangle_height = 50, 120

        if character == Character.RYU:
            body_rectangle_width = 46
            body_rectangle_height = 102

        return [body_rectangle_width, body_rectangle_height]
