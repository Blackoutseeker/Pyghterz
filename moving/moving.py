import pygame

clock = pygame.time.Clock()
FPS = 60
speed = 0.8


class Moving:
    def __init__(self):
        self.position_x = 0
        self.position_y = 0

    def update(self, delta_time):

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.position_y -= speed * delta_time
        if keys[pygame.K_s]:
            self.position_y += speed * delta_time
        if keys[pygame.K_a]:
            self.position_x -= speed * delta_time
        if keys[pygame.K_d]:
            self.position_x += speed * delta_time
