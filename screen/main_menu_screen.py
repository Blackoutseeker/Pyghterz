from .screen import Screen, ScreenType
from pygame import Surface, QUIT, quit, KEYDOWN, K_ESCAPE, K_RETURN, Rect, draw
from font import CustomFont
from os import path
from pygame.image import load as load_image
from sys import exit
from typing import List
from pygame.event import Event
from input import QuizKeymap
from audio import SoundType, AudioManager
from utils import Dimensions, Config


class MainMenuScreen(Screen):
    def __init__(self, screen: Surface):
        super().__init__(screen)
        self._custom_font: CustomFont = CustomFont()
        self._background_image: Surface = self._load_image('BACKGROUND')
        self._keymap_image: Surface = self._load_image('KEYMAP')
        self._show_keymap: bool = False
        self._current_button: int = 0

    @staticmethod
    def _load_image(image_name: str) -> Surface:
        base_path: str = path.dirname(path.dirname(__file__))
        image_path: str = f'assets/images/sprites/menu/{image_name}.png'
        image_path = path.join(base_path, image_path)
        image: Surface = load_image(image_path)
        return image

    @staticmethod
    def _play_sound_by_type(sound_type: SoundType):
        AudioManager.play_sound_by_type(sound_type)

    def handle_events(self, events: List[Event]):
        for event in events:
            if event.type == QUIT:
                quit()
                exit()
            elif event.type == KEYDOWN:
                player1_keys = QuizKeymap.Player1
                player2_keys = QuizKeymap.Player2

                if event.key == K_ESCAPE:
                    if self._show_keymap:
                        self._play_sound_by_type(SoundType.SELECTED)
                        self._show_keymap = False
                    else:
                        quit()
                        exit()

                elif ((event.key == player1_keys.UP.value or event.key == player2_keys.UP.value)
                      and not self._show_keymap):
                    self._current_button = (self._current_button - 1) % 3
                    self._play_sound_by_type(SoundType.OPTION_CHANGE)
                elif ((event.key == player1_keys.DOWN.value or event.key == player2_keys.DOWN.value)
                      and not self._show_keymap):
                    self._current_button = (self._current_button + 1) % 3
                    self._play_sound_by_type(SoundType.OPTION_CHANGE)

                elif (event.key in player1_keys.CONFIRM_BUTTONS.value or
                      event.key in player2_keys.CONFIRM_BUTTONS.value or
                      event.key == K_RETURN) and not self._show_keymap:
                    if self._current_button == 0:
                        self._play_sound_by_type(SoundType.SELECTED)
                        return ScreenType.QUIZ.name
                    elif self._current_button == 1:
                        self._play_sound_by_type(SoundType.SELECTED)
                        self._show_keymap = True
                    elif self._current_button == 2:
                        self._play_sound_by_type(SoundType.SELECTED)
                        quit()
                        exit()

                elif (event.key in player1_keys.CANCEL_BUTTONS.value or
                      event.key in player2_keys.CANCEL_BUTTONS.value) and self._show_keymap:
                    self._play_sound_by_type(SoundType.SELECTED)
                    self._show_keymap = False

    def render(self):
        white_color: tuple[int, int, int] = (255, 255, 255)
        black_color: tuple[int, int, int] = (0, 0, 0)
        red_color: tuple[int, int, int] = (255, 0, 0)

        self.screen.fill(white_color)
        self.screen.blit(self._background_image, (0, 0))

        version_font = self._custom_font.render_font(Config.VERSION.value, 12, black_color, (0, 0))
        self.screen.blit(version_font, (20, Dimensions.SCREEN_HEIGHT.value - 30))

        center_position_x = Dimensions.SCREEN_WIDTH.value // 2
        center_position_y = Dimensions.SCREEN_HEIGHT.value // 2

        rectangle_width = Dimensions.SCREEN_WIDTH.value - 400
        rectangle_height = 60
        spacing = 20

        def draw_button(text_str, center_x, center_y, button: int):
            text = self._custom_font.render_font(text_str, 14, white_color, (0, 0))
            text_rect = text.get_rect(center=(center_x, center_y))

            rect_x = center_x - (rectangle_width // 2)
            rect_y = center_y - (rectangle_height // 2)
            rect = Rect(rect_x, rect_y, rectangle_width, rectangle_height)

            color = black_color
            if button == self._current_button:
                color = red_color
            draw.rect(self.screen, black_color, rect)
            draw.rect(self.screen, color, rect, 5)
            self.screen.blit(text, text_rect)

        draw_button('Iniciar jogo!', center_position_x, center_position_y, 0)

        second_button_y = center_position_y + rectangle_height + spacing
        draw_button('Controles', center_position_x, second_button_y, 1)

        third_button_y = second_button_y + rectangle_height + spacing
        draw_button('Sair', center_position_x, third_button_y, 2)

        if self._show_keymap:
            self.screen.blit(self._keymap_image, (0, 0))
