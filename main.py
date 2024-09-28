import pygame
from sys import exit
from state import PlayerState
from sprite import Animation
from utils import Character
from input import Movement

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pyghterz')

clock = pygame.time.Clock()
FPS = 60
sprite_scale = 2.0
animation_speed = 0.2
player_state = PlayerState()
animation = Animation(Character.RYU, sprite_scale, animation_speed, screen, player_state)
movement = Movement(player_state)


def game_loop():
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        screen.fill((0, 0, 0,))
        movement.update()
        animation.render(movement.position_x, movement.position_y)
        pygame.display.flip()
    pygame.quit()
    exit()


if __name__ == '__main__':
    game_loop()
