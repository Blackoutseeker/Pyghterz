import pygame
from sys import exit
from moving import Moving

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pygtherz')

FPS = 60
clock = pygame.time.Clock()
moving = Moving()

img = pygame.image.load("C:\\Python\\Pyghterz\\assets\\images\\sprites\\characters\\RYU\\IDLE\\0.png")


def game_loop():
    running = True
    while running:
        for event in pygame.event.get():
            delta_time = clock.get_time()
            moving.update(delta_time)
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        screen.fill((0, 0, 0,))
        screen.blit(img, (moving.position_x, moving.position_y))
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
    exit()


if __name__ == '__main__':
    game_loop()
