import pygame
from sys import exit
from state import PlayerState
from sprite import Animation
from utils import Character
from moving import Moving

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pyghterz')

FPS = 60
clock = pygame.time.Clock()
sprite_scale = 2.0
animation_speed = 0.2
player_state = PlayerState()
animation = Animation(Character.RYU, sprite_scale, animation_speed, screen, player_state)
moving = Moving(player_state)


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

        moving.update()
        screen.fill((0, 0, 0,))
        animation.render(moving.position_x, moving.position_y)
        pygame.display.flip()
    pygame.quit()
    exit()


if __name__ == '__main__':
    game_loop()
