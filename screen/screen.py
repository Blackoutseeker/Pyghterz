from enum import Enum
from pygame import Surface
from typing import List
from pygame.event import Event


class ScreenType(Enum):
    MAIN_MENU = 'MAIN_MENU'
    QUIZ = 'QUIZ'
    GAMEPLAY = 'GAMEPLAY'


class Screen:
    def __init__(self, screen: Surface):
        self.screen = screen

    def handle_events(self, events: List[Event]):
        pass

    def update(self):
        pass

    def render(self):
        pass
