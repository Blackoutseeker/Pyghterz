from enum import Enum
from pygame import Surface, image, Rect, transform, draw
from state import PlayerState
from utils import Dimensions
from os import path


class _HealthBarColor(Enum):
    GREEN = (0, 255, 0)
    YELLOW = (255, 255, 0)
    ORANGE = (255, 165, 0)


class Hud:
    def __init__(self, screen: Surface, player1_state: PlayerState, player2_state: PlayerState):
        self._screen: Surface = screen
        self._player1_state: PlayerState = player1_state
        self._player2_state: PlayerState = player2_state

        self._player1_portrait: Surface = Surface((0, 0))
        self._player2_portrait: Surface = Surface((0, 0))

        self._player1_health_bar: Surface = Surface((0, 0))
        self._player2_health_bar: Surface = Surface((0, 0))

        self._player1_rectangle_health_bar: Rect = Surface((0, 0)).fill(_HealthBarColor.GREEN.value)
        self._player2_rectangle_health_bar: Rect = Surface((0, 0)).fill(_HealthBarColor.GREEN.value)

        self._player1_rectangle_health_bar.update((80, 26, 280, 18))
        self._player2_rectangle_health_bar.update((Dimensions.SCREEN_WIDTH.value - (280 + 80), 26, 280, 18))

        self._load_sprites()

    def _load_sprites(self):
        base_path: str = path.dirname(path.dirname(__file__))
        sprites_path: str = 'assets/images/sprites'
        portrait_path: str = 'portrait'
        portrait_path = path.join(base_path, sprites_path, portrait_path)

        player1_character: str = self._player1_state.get_character().value
        player2_character: str = self._player2_state.get_character().value

        player1_portrait_image: Surface = image.load(f'{portrait_path}/{player1_character}.png')
        player2_portrait_image: Surface = image.load(f'{portrait_path}/{player2_character}.png')

        self._player1_portrait = player1_portrait_image
        self._player2_portrait = transform.flip(player2_portrait_image, True, False)

        hud_path: str = 'hud'
        hud_path = path.join(base_path, sprites_path, hud_path)
        hud_image: Surface = image.load(f'{hud_path}/hud.png')

        self._player1_health_bar = hud_image
        hud_image_flipped = transform.flip(hud_image, True, False)
        self._player2_health_bar = hud_image_flipped

    def render(self):
        self._screen.blit(self._player1_portrait, (16, 24))
        player2_portrait_width: int = self._player2_portrait.get_width()
        player2_portrait_position_x: float = Dimensions.SCREEN_WIDTH.value - (player2_portrait_width + 16)
        self._screen.blit(self._player2_portrait, (player2_portrait_position_x, 24))

        player1_health_bar_color: tuple[int, int, int] = _HealthBarColor.GREEN.value
        player2_health_bar_color: tuple[int, int, int] = _HealthBarColor.GREEN.value

        draw.rect(self._screen, player1_health_bar_color, self._player1_rectangle_health_bar)
        self._screen.blit(self._player1_health_bar, (10, 10))

        draw.rect(self._screen, player2_health_bar_color, self._player2_rectangle_health_bar)
        player2_health_bar_width: int = self._player2_health_bar.get_width()
        player2_health_bar_position_x: float = Dimensions.SCREEN_WIDTH.value - (player2_health_bar_width + 10)
        self._screen.blit(self._player2_health_bar, (player2_health_bar_position_x, 10))
