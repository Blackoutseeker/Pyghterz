from .screen import Screen, ScreenType
from pygame import Surface, QUIT, quit, KEYDOWN, K_ESCAPE, K_RETURN
from sys import exit
from typing import List
from pygame.event import Event
from font import CustomFont
from utils import Dimensions


class MainMenuScreen(Screen):
    def __init__(self, screen: Surface):
        super().__init__(screen)
        self._custom_font: CustomFont = CustomFont()

    def handle_events(self, events: List[Event]):
        for event in events:
            if event.type == QUIT:
                quit()
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
                    exit()
                elif event.key == K_RETURN:
                    return ScreenType.QUIZ.name

    def render(self):
        self.screen.fill((0, 0, 0))
        position_x, position_y = Dimensions.SCREEN_WIDTH.value // 2, Dimensions.SCREEN_HEIGHT.value // 2
        text = self._custom_font.render_font('Press Enter to start!', 14,
                                             (255, 255, 255), (position_x, position_y))
        self.screen.blit(text, (position_x, position_y))
