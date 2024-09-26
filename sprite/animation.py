from utils import Character, PlayerAction
from state import PlayerState
from os import path, listdir
from pygame import image, Surface, transform
from typing import List


class Animation:
    def __init__(self, character: Character, scale: float, speed: float, screen: Surface, player_state: PlayerState):
        self.character: Character = character
        self.scale: float = scale
        self.speed: float = speed
        self.screen: Surface = screen
        self.player_state: PlayerState = player_state
        self._sprite_index: int = 0
        self.sprites: dict = {}
        for action in PlayerAction:
            self.sprites[action.name] = self._load_sprites(action)

    def _load_sprites(self, player_action: PlayerAction) -> List[Surface]:
        sprites: List[Surface] = []
        base_path = path.dirname(path.dirname(__file__))
        sprites_path: str = f'assets/images/sprites/characters/{self.character.name}/{player_action.name}'
        sprites_path = path.join(base_path, sprites_path)
        files: List[str] = listdir(sprites_path)
        for file in files:
            sprite: Surface = image.load(f'{sprites_path}/{file}')
            width, height = sprite.get_size()
            scaled_sprite: Surface = transform.scale(sprite, (int(width * self.scale), int(height * self.scale)))
            sprites.append(scaled_sprite)
        return sprites

    def render(self, position_x: float, position_y: float):
        self._sprite_index += self.speed
        current_sprites: List[Surface] = self.sprites[self.player_state.get_player_action().name]
        if self._sprite_index >= len(current_sprites):
            self._sprite_index = 0
        self.screen.blit(current_sprites[int(self._sprite_index)], (position_x, position_y))
