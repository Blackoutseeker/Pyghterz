from pygame import Rect, Surface
from utils import Dimensions


class Viewport:
    def __init__(self, screen: Surface):
        self._screen: Surface = screen
        self._viewport: Rect = Rect(0, 0, Dimensions.SCREEN_WIDTH.value, Dimensions.SCREEN_HEIGHT.value)
        self._world_width: int = Dimensions.WORLD_WIDTH.value
        self._world_height: int = Dimensions.WORLD_HEIGHT.value
        self._left = self._viewport.left
        self._right = self._viewport.right

    def update(self, player1_position_x: float, player2_position_x: float, world_width: int):
        center_x = (player1_position_x + player2_position_x) / 2
        self._viewport.center = (center_x, self._viewport.centery)
        self.clamp_to_world(world_width)

    def clamp_to_world(self, world_width: int):
        if self._viewport.left < 0:
            self._viewport.left = 0
        if self._viewport.right > world_width:
            self._viewport.right = world_width

    def apply(self, position_x: float, position_y: float):
        return position_x - self._viewport.x, position_y - self._viewport.y

    def get_viewport(self) -> Rect:
        return self._viewport
