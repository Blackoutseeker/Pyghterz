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

player1_state = PlayerState()
player2_state = PlayerState()

animation1 = Animation(Character.RYU, sprite_scale, animation_speed, screen, player1_state)
animation2 = Animation(Character.RYU, sprite_scale, animation_speed, screen, player2_state)

movement1 = Movement(player1_state)
movement2 = Movement(player2_state, True)


def game_loop():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        screen.fill((0, 0, 0,))

        movement1.update()
        movement2.update()

        animation1.render(movement1.get_position_x(), movement1.get_position_y())
        animation2.render(movement2.get_position_x(), movement2.get_position_y())

        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
    exit()


if __name__ == '__main__':
    game_loop()
