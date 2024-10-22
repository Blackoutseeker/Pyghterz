import pygame
from sys import exit
from state import PlayerState, Scenery, Viewport
from sprite import Animation
from utils import Character, Dimensions, Config
from input import Movement
from audio import AudioManager
from collision import Hitbox

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

player1_hitbox = Hitbox(Character.RYU, player1_state, Config.SPRITE_SCALE.value, screen)
player2_hitbox = Hitbox(Character.RYU, player2_state, Config.SPRITE_SCALE.value, screen)

audio_manager = AudioManager()
audio_manager.load()
# audio_manager.play_background_music()


def handle_players_flip():
    player1_x, _ = player1_state.get_player_position()
    player2_x, _ = player2_state.get_player_position()
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

        movement1.update(audio_manager)
        movement2.update(audio_manager)
        player1_position_x, player1_position_y = player1_state.get_player_position()
        player2_position_x, player2_position_y = player2_state.get_player_position()

        viewport.update(player1_position_x, player2_position_x, Dimensions.WORLD_WIDTH.value)

        scenery.render(-viewport.get_viewport().left, 0, viewport)

        handle_players_flip()

        animation1.render(player1_position_x - viewport.get_viewport().left, player1_position_y,
                          viewport.get_viewport())
        animation2.render(player2_position_x - viewport.get_viewport().left, player2_position_y,
                          viewport.get_viewport())

        player1_hitbox.render()
        player2_hitbox.render()

        pygame.display.flip()
        clock.tick(Config.FPS.value)
    audio_manager.dispose()
    pygame.quit()
    exit()


if __name__ == '__main__':
    game_loop()
