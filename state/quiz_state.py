from utils import Character
from typing import List


class QuizState:
    def __init__(self, character: Character, is_second_player: bool = False):
        self._character: Character = character
        self._is_second_player = is_second_player
        self._percentage_balance: float = 0
        self._score: int = 0
        self._characters_used: List[Character] = [character]

    def get_is_second_player(self) -> bool:
        return self._is_second_player

    def get_character(self) -> Character:
        return self._character

    def get_percentage_balance(self):
        return self._percentage_balance

    def set_percentage_balance(self, percentage: float):
        self._percentage_balance = percentage

    def get_score(self):
        return self._score

    def increase_score(self, score: int):
        self._score += score

    def get_characters_used(self) -> List[Character]:
        return self._characters_used

    def add_character_used(self, character: Character):
        self._characters_used.append(character)

    def reset_all_states(self):
        self._character = Character.RYU
        self._percentage_balance = 0
        self._score = 0
        self._characters_used = []
