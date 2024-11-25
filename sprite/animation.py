from utils import Character, PlayerAction
from state import PlayerState
from os import path, listdir
from pygame import image, Surface, transform, Rect
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
        self._play_loop: bool = False
        self._index_loop: int = 0

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

    def render(self, position_x: float, position_y: float, viewport: Rect):
        sprite_index: int = self._player_state.get_sprite_index()
        current_sprites: List[Surface] = self._sprites[self._player_state.get_player_action().name]

        if get_ticks() - self._player_state.get_animation_update_time() > self._speed:
            sprite_index += 1
            if self._play_loop:
                if sprite_index >= len(current_sprites):
                    sprite_index = self._index_loop
            self._player_state.set_sprite_index(sprite_index)
            self._player_state.set_animation_update_time(get_ticks())

        is_player_attacking: bool = self._player_state.get_is_attacking()
        is_player_getting_hit: bool = (self._player_state.get_is_getting_weak_hit() or
                                       self._player_state.get_is_getting_medium_hit() or
                                       self._player_state.get_is_getting_high_hit())
        is_player_blocking: bool = self._player_state.get_is_blocking()
        player_won: bool = self._player_state.get_win()
        player_lose: bool = self._player_state.get_lose()

        if player_won or player_lose:
            if player_won:
                self._play_loop = True
                self._index_loop = 9
            if player_lose:
                self._play_loop = True
                self._index_loop = 10
                current_sprites = self._sprites[PlayerAction.DEFEAT.name]
                self._index_loop = len(current_sprites) - 1

        if sprite_index >= len(current_sprites):
            if is_player_attacking:
                self._player_state.set_is_attacking(False)
            if is_player_getting_hit:
                self._player_state.set_is_getting_weak_hit(False)
                self._player_state.set_is_getting_medium_hit(False)
                self._player_state.set_is_getting_high_hit(False)
            if is_player_blocking:
                self._play_loop = True
                self._index_loop = len(current_sprites) - 1
            else:
                self._play_loop = False
                self._index_loop = 0
            current_sprites = self._sprites[PlayerAction.IDLE.name]
            self._player_state.reset_animation_attributes()
            sprite_index = 0

        current_sprite: Surface = current_sprites[sprite_index]

        if not self._player_state.get_is_facing_right():
            current_sprite = transform.flip(current_sprite, True, False)

        adjusted_x = position_x - viewport.left
        adjusted_y = position_y - viewport.top

        self._screen.blit(current_sprite, (adjusted_x, adjusted_y))
