import pygame
from sys import exit
from state import PlayerState, Scenery, Viewport
from sprite import Animation
from utils import Character, Dimensions, Config
from input import Movement

pygame.init()

screen = pygame.display.set_mode((Dimensions.SCREEN_WIDTH.value, Dimensions.SCREEN_HEIGHT.value))
pygame.display.set_caption('Pyghterz')

viewport = Viewport(screen)
clock = pygame.time.Clock()

sprite_scale = Config.SPRITE_SCALE.value
animation_speed = Config.ANIMATION_SPEED.value
scenery_scale = Config.SCENERY_SCALE.value
scenery_speed = Config.SCENERY_SPEED.value

scenery = Scenery(scenery_scale, scenery_speed, screen)
player1_state = PlayerState()
player2_state = PlayerState()

animation1 = Animation(Character.RYU, sprite_scale, animation_speed, screen, player1_state)
animation2 = Animation(Character.RYU, sprite_scale, animation_speed, screen, player2_state)

movement1 = Movement(player1_state)
movement2 = Movement(player2_state, True)


def handle_players_flip():
    player1_x = movement1.get_position_x()
    player2_x = movement2.get_position_x()
    if player1_x < player2_x:
        player1_state.set_is_facing_right(True)
        player2_state.set_is_facing_right(False)
    else:
        player1_state.set_is_facing_right(False)
        player2_state.set_is_facing_right(True)


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
        
        viewport.update(movement1.get_position_x(), movement2.get_position_x(), Dimensions.WORLD_WIDTH.value)

        scenery.render(-viewport.get_viewport().left, 0, viewport)

        handle_players_flip()

        animation1.render(movement1.get_position_x() - viewport.get_viewport().left, movement1.get_position_y(),
                          viewport.get_viewport())
        animation2.render(movement2.get_position_x() - viewport.get_viewport().left, movement2.get_position_y(),
                          viewport.get_viewport())

        pygame.display.flip()
        clock.tick(Config.FPS.value)
    pygame.quit()
    exit()


if __name__ == '__main__':
    game_loop()
