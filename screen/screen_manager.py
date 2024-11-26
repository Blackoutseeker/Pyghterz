from pygame import Surface
from .screen import ScreenType
from .main_menu_screen import MainMenuScreen
from .gameplay_screen import GameplayScreen
from .quiz_screen import QuizScreen
from typing import List
from pygame.event import Event


class ScreenManager:
    def __init__(self, screen: Surface):
        self.screen = screen
        self._screens: dict = {
            f'{ScreenType.MAIN_MENU.name}': MainMenuScreen(screen),
            f'{ScreenType.GAMEPLAY.name}': GameplayScreen(screen),
            f'{ScreenType.QUIZ.name}': QuizScreen(screen),
        }
        self._current_screen: str = ScreenType.MAIN_MENU.name

    def handle_events(self, events: List[Event]):
        next_screen: str = self._screens[self._current_screen].handle_events(events)
        if next_screen:
            self._current_screen = next_screen

    def update(self):
        self._screens[self._current_screen].update()

    def render(self):
        self._screens[self._current_screen].render()
