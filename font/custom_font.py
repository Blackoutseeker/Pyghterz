from pygame.font import Font
from os import path
from pygame import Surface


class CustomFont:
    def __init__(self):
        self._font_path: str = self._get_font_path()

    @staticmethod
    def _get_font_path() -> str:
        base_path: str = path.dirname(path.dirname(__file__))
        font_path: str = path.join(base_path, 'assets/fonts/PressStart2P-Regular.ttf')
        return font_path

    def render_font(self, text: str, size: int, color: tuple[int, int, int], position: tuple[int, int]) -> Surface:
        font = Font(self._font_path, size)
        text_surface: Surface = font.render(text, True, color)
        return text_surface
