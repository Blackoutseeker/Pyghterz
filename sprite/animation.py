from utils import Character, PlayerAction
from state import PlayerState
from os import path, listdir
from pygame import image, Surface, transform
from pygame.time import get_ticks
from typing import List


class Animation:
    def __init__(self, character: Character, scale: float, speed: float, screen: Surface, player_state: PlayerState):
        self._character: Character = character
        self._scale: float = scale
        self._speed: float = speed
        self._screen: Surface = screen
        self._player_state: PlayerState = player_state
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
        sprite_index: int = self._player_state.get_sprite_index()
        current_sprites: List[Surface] = self._sprites[self._player_state.get_player_action().name]
        if get_ticks() - self._player_state.get_animation_update_time() > self._speed:
            sprite_index += 1
            self._player_state.set_sprite_index(sprite_index)
            self._player_state.set_animation_update_time(get_ticks())

        sprite_index = self._player_state.get_sprite_index()
        is_player_attacking: bool = self._player_state.get_is_attacking()
        if sprite_index >= len(current_sprites):
            if is_player_attacking:
                self._player_state.set_is_attacking(False)
                current_sprites = self._sprites[PlayerAction.IDLE.name]
            self._player_state.reset_animation_attributes()
            sprite_index = 0

        current_sprite: Surface = current_sprites[sprite_index]
        if self._player_state.get_is_facing_right() is not True:
            current_sprite = transform.flip(current_sprite, True, False)
        self._screen.blit(current_sprite, (position_x, position_y))
