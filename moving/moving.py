import pygame
from state import PlayerState
from utils import PlayerAction

speed = 700


class Moving:
    def __init__(self, player_state: PlayerState):
        self.position_x = 0
        self.position_y = 0
        self.player_state: PlayerState = player_state

    def update(self, delta_time):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.position_y -= speed * delta_time
        elif keys[pygame.K_s]:
            self.position_y += speed * delta_time
        elif keys[pygame.K_a]:
            self.position_x -= speed * delta_time
            self.player_state.set_player_action(PlayerAction.MOVE_BACKWARD)
        elif keys[pygame.K_d]:
            self.position_x += speed * delta_time
            self.player_state.set_player_action(PlayerAction.MOVE_FORWARD)
        else:
            self.player_state.set_player_action(PlayerAction.IDLE)
