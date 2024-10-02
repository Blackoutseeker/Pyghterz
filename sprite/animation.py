from utils import Character, PlayerAction
from state import PlayerState
from os import path, listdir
from pygame import image, Surface, transform
from typing import List


class Animation:
    def __init__(self, character: Character, scale: float, speed: float, screen: Surface, player_state: PlayerState):
        self._character: Character = character
        self._scale: float = scale
        self._speed: float = speed
        self._screen: Surface = screen
        self._player_state: PlayerState = player_state
        self._sprite_index: int = 0
        self._sprites: dict = {}
        for action in PlayerAction:
            self._sprites[action.name] = self._load_sprites(action)

    def _load_sprites(self, player_action: PlayerAction) -> List[Surface]:
        sprites: List[Surface] = []
        base_path = path.dirname(path.dirname(__file__))
        sprites_path: str = f'assets/images/sprites/characters/{self._character.name}/{player_action.name}'
        sprites_path = path.join(base_path, sprites_path)
        files: List[str] = listdir(sprites_path)
        for file in files:
            sprite: Surface = image.load(f'{sprites_path}/{file}')
            width, height = sprite.get_size()
            scaled_sprite: Surface = transform.scale(sprite, (int(width * self._scale), int(height * self._scale)))
            sprites.append(scaled_sprite)
        return sprites

    def render(self, position_x: float, position_y: float):
        self._sprite_index += self._speed
        current_sprites: List[Surface] = self._sprites[self._player_state.get_player_action().name]
        is_player_attacking: bool = self._player_state.get_is_attacking()
        if is_player_attacking is True:
            if int(self._sprite_index) >= len(current_sprites):
                self._player_state.set_is_attacking(False)
                self._sprite_index = 0
        if self._sprite_index >= len(current_sprites):
            self._sprite_index = 0
        self._screen.blit(current_sprites[int(self._sprite_index)], (position_x, position_y))
