import pygame
from sys import exit
from state import PlayerState, Scenery, Viewport
from sprite import Animation
from utils import Character, Dimensions, Config
from input import Movement
from audio import AudioManager
from collision import Hitbox, Detection


class Game:
    def __init__(self):
        pygame.init()

        self._display_flags = pygame.SCALED | pygame.RESIZABLE
        self._screen = pygame.display.set_mode((Dimensions.SCREEN_WIDTH.value, Dimensions.SCREEN_HEIGHT.value),
                                               flags=self._display_flags, vsync=1)
        pygame.display.set_caption('Pyghterz')

        self._viewport = Viewport(self._screen)
        self._clock = pygame.time.Clock()

        self._sprite_scale = Config.SPRITE_SCALE.value
        self._animation_speed = Config.ANIMATION_SPEED.value
        self._scenery_scale = Config.SCENERY_SCALE.value
        self._scenery_speed = Config.SCENERY_SPEED.value

        self._scenery = Scenery(self._scenery_scale, self._scenery_speed, self._screen)
        self._player1_state = PlayerState()
        self._player2_state = PlayerState()

        self._animation1 = Animation(Character.RYU, self._sprite_scale, self._animation_speed,
                               self._screen, self._player1_state)
        self._animation2 = Animation(Character.RYU, self._sprite_scale, self._animation_speed,
                               self._screen, self._player2_state)

        self._movement1 = Movement(self._player1_state)
        self._movement2 = Movement(self._player2_state, True)

        self._player1_hitbox = Hitbox(Character.RYU, self._player1_state, Config.SPRITE_SCALE.value, self._screen)
        self._player2_hitbox = Hitbox(Character.RYU, self._player2_state, Config.SPRITE_SCALE.value, self._screen)

        self._detection = Detection(self._player1_state, self._player2_state)

        self._audio_manager = AudioManager()
        self._audio_manager.load()
        # self._audio_manager.play_background_music()

    def _handle_players_flip(self):
        player1_x, _ = self._player1_state.get_player_position()
        player2_x, _ = self._player2_state.get_player_position()
        if player1_x < player2_x:
            self._player1_state.set_is_facing_right(True)
            self._player2_state.set_is_facing_right(False)
        else:
            self._player1_state.set_is_facing_right(False)
            self._player2_state.set_is_facing_right(True)

    def _handle_players_z_axis(self, player1_position_x: float, player2_position_x: float,
                               player1_position_y: float, player2_position_y: float):
        is_player1_attacking = self._player1_state.get_is_attacking()
        if is_player1_attacking:
            self._animation2.render(player2_position_x - self._viewport.get_viewport().left, player2_position_y,
                                    self._viewport.get_viewport())
            self._animation1.render(player1_position_x - self._viewport.get_viewport().left, player1_position_y,
                                    self._viewport.get_viewport())
        else:
            self._animation1.render(player1_position_x - self._viewport.get_viewport().left, player1_position_y,
                                    self._viewport.get_viewport())
            self._animation2.render(player2_position_x - self._viewport.get_viewport().left, player2_position_y,
                                    self._viewport.get_viewport())

    def run(self):
        running = True
        self._screen.fill((0, 0, 0))
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False


            self._movement1.update(self._audio_manager)
            self._movement2.update(self._audio_manager)
            player1_position_x, player1_position_y = self._player1_state.get_player_position()
            player2_position_x, player2_position_y = self._player2_state.get_player_position()

            self._viewport.update(player1_position_x, player2_position_x, Dimensions.WORLD_WIDTH.value)

            self._scenery.render(-self._viewport.get_viewport().left, 0, self._viewport)

            self._handle_players_flip()
            self._handle_players_z_axis(player1_position_x, player2_position_x, player1_position_y, player2_position_y)

            self._player1_hitbox.render()
            self._player2_hitbox.render()

            player1_body_rectangle = self._player1_hitbox.get_body_rectangle()
            player1_attack_rectangle = self._player1_hitbox.get_attack_rectangle()
            player2_body_rectangle = self._player2_hitbox.get_body_rectangle()
            player2_attack_rectangle = self._player2_hitbox.get_attack_rectangle()

            self._detection.detect_collision(player1_body_rectangle, player2_body_rectangle,
                                       player1_attack_rectangle, player2_attack_rectangle)

            pygame.display.flip()
            self._clock.tick(Config.FPS.value)
        self._audio_manager.dispose()
        pygame.quit()
        exit()
