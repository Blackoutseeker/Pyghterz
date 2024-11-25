import pygame
from sys import exit
from state import PlayerState, Scenery, Viewport
from sprite import Animation, Hud
from utils import Dimensions, Config, Character, PlayerAction
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
        self._player1_state = PlayerState(Character.RYU)
        self._player2_state = PlayerState(Character.RYU, True)

        self._animation1 = Animation(Character.RYU, self._sprite_scale, self._animation_speed,
                                     self._screen, self._player1_state)
        self._animation2 = Animation(Character.RYU, self._sprite_scale, self._animation_speed,
                                     self._screen, self._player2_state)

        self._movement1 = Movement(self._player1_state, self._player2_state)
        self._movement2 = Movement(self._player2_state, self._player1_state, True)

        self._player1_hitbox = Hitbox(Character.RYU, self._player1_state, Config.SPRITE_SCALE.value, self._screen)
        self._player2_hitbox = Hitbox(Character.RYU, self._player2_state, Config.SPRITE_SCALE.value, self._screen)

        self._detection = Detection(self._player1_state, self._player2_state)
        self._hud = Hud(self._screen, self._player1_state, self._player2_state)

        self._audio_manager = AudioManager()
        self._audio_manager.load()
        # self._audio_manager.play_background_music()

        self._round_ended: bool = False
        self._double_defeat: bool = False
        self._is_players_colliding: bool = False
        self._reset_event: int = pygame.USEREVENT + 1
        self._event_created: bool = False

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

    def _handle_players_health(self):
        player1_health: float = self._player1_state.get_health()
        player2_health: float = self._player2_state.get_health()

        if player1_health <= 0 and player2_health <= 0:
            self._double_defeat = True
            self._round_ended = True
            self._player1_state.set_lose(True)
            self._player2_state.set_lose(True)
            self._player1_state.set_player_action(PlayerAction.DEFEAT)
            self._player2_state.set_player_action(PlayerAction.DEFEAT)
            return
        if player1_health <= 0 or player2_health <= 0:
            self._round_ended = True
        if player1_health <= 0:
            self._player1_state.set_lose(True)
            self._player2_state.set_win(True)
            self._player1_state.set_player_action(PlayerAction.DEFEAT)
            self._player2_state.set_player_action(PlayerAction.WIN)
        if player2_health <= 0:
            self._player2_state.set_lose(True)
            self._player1_state.set_win(True)
            self._player2_state.set_player_action(PlayerAction.DEFEAT)
            self._player1_state.set_player_action(PlayerAction.WIN)

    def _handle_reset(self):
        self._round_ended = False
        self._player1_state.reset_all_states()
        self._player2_state.reset_all_states()

    def run(self):
        running = True
        self._screen.fill((0, 0, 0))
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == self._reset_event:
                    self._handle_reset()
                    pygame.time.set_timer(self._reset_event, 0)
                    self._event_created = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            self._movement1.update(self._round_ended, self._is_players_colliding, self._audio_manager)
            self._movement2.update(self._round_ended, self._is_players_colliding, self._audio_manager)

            player1_position_x, player1_position_y = self._player1_state.get_player_position()
            player2_position_x, player2_position_y = self._player2_state.get_player_position()

            self._viewport.update(player1_position_x, player2_position_x, Dimensions.WORLD_WIDTH.value)
            self._scenery.render(-self._viewport.get_viewport().left, 0, self._viewport)

            self._hud.render()
            self._handle_players_flip()
            self._handle_players_z_axis(player1_position_x, player2_position_x, player1_position_y, player2_position_y)
            self._handle_players_health()

            self._player1_hitbox.render()
            self._player2_hitbox.render()

            player1_body_rectangle = self._player1_hitbox.get_body_rectangle()
            player1_attack_rectangle = self._player1_hitbox.get_attack_rectangle()
            player2_body_rectangle = self._player2_hitbox.get_body_rectangle()
            player2_attack_rectangle = self._player2_hitbox.get_attack_rectangle()

            self._detection.detect_collision(player1_body_rectangle, player2_body_rectangle,
                                             player1_attack_rectangle, player2_attack_rectangle)
            is_players_colliding: bool = Detection.get_players_collision(player1_body_rectangle, player2_body_rectangle)
            self._is_players_colliding = is_players_colliding

            if self._round_ended and not self._event_created:
                pygame.time.set_timer(self._reset_event, 7000)
                self._event_created = True
            pygame.display.flip()
            self._clock.tick(Config.FPS.value)
        self._audio_manager.dispose()
        pygame.quit()
        exit()
