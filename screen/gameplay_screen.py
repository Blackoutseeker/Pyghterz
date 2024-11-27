from .screen import Screen, ScreenType
import pygame
from sys import exit
from state import QuizState, PlayerState, Scenery, Viewport
from sprite import Animation, Hud
from utils import Config, Character, PlayerAction
from input import Movement
from audio import AudioManager
from collision import Hitbox, Detection
from pygame.event import Event
from typing import List


class GameplayScreen(Screen):
    def __init__(self, screen: pygame.Surface, player1_quiz_state: QuizState, player2_quiz_state: QuizState):
        super().__init__(screen)
        self._screen = screen

        self._viewport = Viewport(self._screen)
        self._clock = pygame.time.Clock()

        self._animation_speed = Config.ANIMATION_SPEED.value
        self._scenery_scale = Config.SCENERY_SCALE.value
        self._scenery_speed = Config.SCENERY_SPEED.value

        self._scenery = Scenery(self._scenery_scale, self._scenery_speed, self._screen)

        self._player1_quiz_state = player1_quiz_state
        self._player2_quiz_state = player2_quiz_state
        self._player1_state = PlayerState(player1_quiz_state)
        self._player2_state = PlayerState(player2_quiz_state)
        self._updated_player_states: bool = False

        self._animation1 = Animation(Character.RYU, self._animation_speed, self._screen, self._player1_state)
        self._animation2 = Animation(Character.RYU, self._animation_speed, self._screen, self._player2_state)

        self._movement1 = Movement(self._player1_state, self._player2_state)
        self._movement2 = Movement(self._player2_state, self._player1_state, True)

        self._player1_hitbox = Hitbox(Character.RYU, self._player1_state, self._screen)
        self._player2_hitbox = Hitbox(Character.RYU, self._player2_state, self._screen)

        self._detection = Detection(self._player1_state, self._player2_state, self._screen)
        self._hud = Hud(self._screen, self._player1_state, self._player2_state)

        self._audio_manager = AudioManager()
        self._audio_manager.load()

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

    def _handle_players_z_axis(self):
        is_player2_attacking = self._player2_state.get_is_attacking()
        top_player_state: PlayerState = self._player1_state
        bottom_player_state: PlayerState = self._player2_state
        bottom_animation: Animation = self._animation2
        top_animation: Animation = self._animation1

        if is_player2_attacking:
            top_player_state = self._player2_state
            bottom_player_state = self._player1_state
            top_animation = self._animation2
            bottom_animation = self._animation1

        bottom_player_position_x, bottom_player_position_y = bottom_player_state.get_player_position()
        top_player_position_x, top_player_position_y = top_player_state.get_player_position()

        bottom_animation.render(bottom_player_position_x, bottom_player_position_y)
        top_animation.render(top_player_position_x, top_player_position_y)

    def _handle_players_health(self):
        player1_health: float = self._player1_state.get_health()
        player2_health: float = self._player2_state.get_health()
        player1_sprite_index: int = self._player1_state.get_sprite_index()
        player2_sprite_index: int = self._player2_state.get_sprite_index()

        if player1_health <= 0 and player2_health <= 0:
            if player1_sprite_index == 0 and player2_sprite_index == 0:
                self._double_defeat = True
                self._round_ended = True
                self._player1_state.set_lose(True)
                self._player2_state.set_lose(True)
                self._player1_state.set_player_action(PlayerAction.DEFEAT)
                self._player2_state.set_player_action(PlayerAction.DEFEAT)
            return
        if player1_health <= 0 or player2_health <= 0:
            if player1_sprite_index == 0 or player2_sprite_index == 0:
                self._round_ended = True
        if player1_health <= 0:
            if player2_sprite_index == 0:
                self._player1_state.set_lose(True)
                self._player2_state.set_win(True)
                self._player1_state.set_player_action(PlayerAction.DEFEAT)
                self._player2_state.set_player_action(PlayerAction.WIN)
        if player2_health <= 0:
            if player1_sprite_index == 0:
                self._player2_state.set_lose(True)
                self._player1_state.set_win(True)
                self._player2_state.set_player_action(PlayerAction.DEFEAT)
                self._player1_state.set_player_action(PlayerAction.WIN)

    def _handle_reset(self):
        self._round_ended = False
        self._double_defeat = False
        self._is_players_colliding = False
        self._player1_state.reset_all_states()
        self._player2_state.reset_all_states()

    def handle_events(self, events: List[Event]):
        for event in events:
            if event.type == pygame.QUIT:
                self._audio_manager.dispose()
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self._handle_reset()
                    return ScreenType.MAIN_MENU.name
            elif event.type == self._reset_event:
                self._handle_reset()
                pygame.time.set_timer(self._reset_event, 0)
                self._event_created = False

    def render(self):
        if not self._updated_player_states:
            self._player1_state.update_states_by_quiz(self._player1_quiz_state)
            self._player2_state.update_states_by_quiz(self._player2_quiz_state)
            self._hud.update_states()
            self._audio_manager.play_background_music()
            self._updated_player_states = True

        player1_body_rectangle = self._player1_hitbox.get_body_rectangle()
        player2_body_rectangle = self._player2_hitbox.get_body_rectangle()

        is_player1_colliding_with_left_wall: bool = (
            self._detection.detect_if_player_is_colliding_with_wall(player1_body_rectangle))
        is_player1_colliding_with_right_wall: bool = (
            self._detection.detect_if_player_is_colliding_with_wall(player1_body_rectangle, True))
        is_player2_colliding_with_left_wall: bool = (
            self._detection.detect_if_player_is_colliding_with_wall(player2_body_rectangle))
        is_player2_colliding_with_right_wall: bool = (
            self._detection.detect_if_player_is_colliding_with_wall(player2_body_rectangle, True))
        is_players_colliding_with_wall: bool = (
            self._detection.get_players_collision_with_wall(player1_body_rectangle, player2_body_rectangle))

        self._movement1.update(self._round_ended, self._is_players_colliding,
                               is_player1_colliding_with_left_wall, is_player1_colliding_with_right_wall,
                               is_players_colliding_with_wall, self._audio_manager)
        self._movement2.update(self._round_ended, self._is_players_colliding,
                               is_player2_colliding_with_left_wall, is_player2_colliding_with_right_wall,
                               is_players_colliding_with_wall, self._audio_manager)

        # player1_position_x, player1_position_y = self._player1_state.get_player_position()
        # player2_position_x, player2_position_y = self._player2_state.get_player_position()

        # self._viewport.update(player1_position_x, player2_position_x, Dimensions.WORLD_WIDTH.value)
        self._scenery.render(0, 0, self._viewport)

        self._hud.render()
        self._handle_players_flip()
        self._handle_players_z_axis()
        self._handle_players_health()

        self._player1_hitbox.render()
        self._player2_hitbox.render()

        player1_attack_rectangle = self._player1_hitbox.get_attack_rectangle()
        player2_attack_rectangle = self._player2_hitbox.get_attack_rectangle()

        self._detection.detect_collision(player1_body_rectangle, player2_body_rectangle,
                                         player1_attack_rectangle, player2_attack_rectangle)
        is_players_colliding: bool = Detection.get_players_collision(player1_body_rectangle, player2_body_rectangle)
        self._is_players_colliding = is_players_colliding

        if self._round_ended and not self._event_created:
            pygame.time.set_timer(self._reset_event, 7000)
            self._event_created = True
