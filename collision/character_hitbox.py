from utils import Character
from pygame import Rect


class CharacterHitbox:
    @staticmethod
    def get_attack_hitboxes(character: Character) -> dict:
        character_attack_hitbox: dict = {}
        if character == Character.RYU:
            character_attack_hitbox: dict = {
                'WEAK_PUNCH': {
                    'start_index': 1,
                    'end_index': 2,
                    'rectangles': [Rect(100, 30, 46, 18), Rect(100, 30, 46, 18), Rect(100, 30, 46, 18)],
                    'mirror_rectangles': [Rect(20, 30, 46, 18), Rect(20, 30, 46, 18), Rect(20, 30, 46, 18)]
                },
                'MEDIUM_PUNCH': {
                    'start_index': 3,
                    'end_index': 5,
                    'rectangles': [Rect(100, 42, 52, 20), Rect(100, 42, 52, 20), Rect(100, 42, 52, 20)],
                    'mirror_rectangles': [Rect(14, 42, 52, 20), Rect(14, 42, 52, 20), Rect(14, 42, 52, 20)]
                },
                'HIGH_PUNCH': {
                    'start_index': 3,
                    'end_index': 5,
                    'rectangles': [Rect(100, 42, 52, 20), Rect(100, 42, 52, 20), Rect(100, 42, 52, 20),],
                    'mirror_rectangles': [Rect(14, 42, 52, 20), Rect(14, 42, 52, 20), Rect(14, 42, 52, 20)]
                },
                'WEAK_KICK': {
                    'start_index': 2,
                    'end_index': 4,
                    'rectangles': [Rect(100, 64, 56, 40), Rect(100, 64, 56, 40), Rect(100, 64, 56, 40),],
                    'mirror_rectangles': [Rect(10, 64, 56, 40), Rect(10, 64, 56, 40), Rect(10, 64, 56, 40),]
                },
                'MEDIUM_KICK': {
                    'start_index': 3,
                    'end_index': 5,
                    'rectangles': [Rect(100, 14, 48, 46), Rect(100, 20, 56, 42), Rect(100, 44, 54, 28),],
                    'mirror_rectangles': [Rect(18, 14, 48, 46), Rect(10, 20, 56, 42), Rect(12, 44, 54, 28),],
                },
                'HIGH_KICK': {
                    'start_index': 3,
                    'end_index': 5,
                    'rectangles': [Rect(100, 14, 48, 46), Rect(100, 20, 56, 42), Rect(100, 44, 54, 28)],
                    'mirror_rectangles': [Rect(18, 14, 48, 46), Rect(10, 20, 56, 42), Rect(12, 44, 54, 28)]
                }
            }

        return character_attack_hitbox
