from pygame import init, Surface, SCALED, RESIZABLE
from pygame.display import set_mode, set_caption, flip
from pygame.time import Clock
from utils import Dimensions, Config
from screen import ScreenManager
from typing import List
from pygame.event import Event, get as get_events


class Game:
    def __init__(self):
        init()
        self._display_flags: int = SCALED | RESIZABLE
        self._screen: Surface = set_mode((Dimensions.SCREEN_WIDTH.value, Dimensions.SCREEN_HEIGHT.value),
                                         self._display_flags, vsync=1)
        set_caption('Pyghterz')
        self._screen_manager: ScreenManager = ScreenManager(self._screen)
        self._clock: Clock = Clock()

    def run(self):
        while True:
            events: List[Event] = get_events()
            self._screen_manager.handle_events(events)
            self._screen_manager.update()
            self._screen_manager.render()
            flip()
            self._clock.tick(Config.FPS.value)
