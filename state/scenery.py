from pygame import Surface, image, transform
from os import path, listdir
from typing import List


class Scenery:
    def __init__(self, scale: float, speed: float, screen: Surface):
        self._scale: float = scale
        self._speed: float = speed
        self._screen: Surface = screen
        self._sprite_index: int = 0
        self._sprites: List[Surface] = self._load_scenery_sprites()

    def _load_scenery_sprites(self) -> List[Surface]:
        sprites: List[Surface] = []
        sprites_path: str = 'C:\\Python\\Pyghterz\\assets\\images\\sprites\\stages\\KEN'
        files: List[str] = listdir(sprites_path)
        for file in files:
            sprite: Surface = image.load(path.join(sprites_path, file))
            width, height = sprite.get_size()
            scaled_sprite: Surface = transform.scale(sprite, (int(width * self._scale), int(height * self._scale)))
            sprites.append(scaled_sprite)
        return sprites

    def render(self, position_x: float, position_y: float):
        self._sprite_index += self._speed
        if self._sprite_index >= len(self._sprites):
            self._sprite_index = 0

        current_sprite: Surface = self._sprites[int(self._sprite_index)]
        self._screen.blit(current_sprite, (position_x, position_y))
