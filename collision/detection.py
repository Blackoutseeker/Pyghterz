from pygame import Rect
from state import PlayerState
from typing import List
from utils import PlayerAction


class Detection:
    def __init__(self, player1_state: PlayerState, player2_state: PlayerState):
        self._player1_state: PlayerState = player1_state
        self._player2_state: PlayerState = player2_state
        self._hit_speed: int = 2

    def detect_collision(self, player1_body_rect: Rect, player2_body_rect: Rect,
                         player1_attack_rect: Rect, player2_attack_rect: Rect):
        self._detect_attack_collision(player1_body_rect, player2_body_rect, player1_attack_rect, player2_attack_rect)
        self._detect_body_collision(player1_body_rect, player2_body_rect)

    def _detect_attack_collision(self, player1_body_rect: Rect, player2_body_rect: Rect,
                                 player1_attack_rect: Rect, player2_attack_rect: Rect):
        is_player1_attacking: bool = player1_attack_rect.colliderect(player2_body_rect)
        is_player2_attacking: bool = player2_attack_rect.colliderect(player1_body_rect)
        damage: int = 20

        if is_player1_attacking:
            player_wins: bool = self._player1_state.get_win()
            if not player_wins:
                player_action_name: str = self._player1_state.get_player_action().name
                damage = self._player1_state.get_attacks_damage()[player_action_name]
                self._change_hit_speed(player_action_name)
        if is_player2_attacking:
            player_wins: bool = self._player2_state.get_win()
            if not player_wins:
                player_action_name: str = self._player2_state.get_player_action().name
                damage = self._player2_state.get_attacks_damage()[player_action_name]
                self._change_hit_speed(player_action_name)

        if is_player1_attacking or is_player2_attacking:
            player_states: List[PlayerState] = [self._player2_state]
            is_both_players_attacking: bool = is_player1_attacking and is_player2_attacking
            is_player1_blocking: bool = self._player1_state.get_is_blocking()
            is_player2_blocking: bool = self._player2_state.get_is_blocking()
            is_players_blocking: bool = is_player1_blocking and is_player2_blocking

            if is_both_players_attacking and not is_players_blocking:
                player_states.append(self._player1_state)
                for player_state in player_states:
                    player_state.set_is_attacking(False)
                    player_state.set_is_getting_weak_hit(True)
                    player_state.set_player_action(PlayerAction.WEAK_HIT)
                    player_state.decrease_health(damage)

            for player_state in player_states:
                if is_player2_attacking:
                    player_state = self._player1_state

                is_player_blocking: bool = player_state.get_is_blocking()
                is_player_getting_hit: bool = self._detect_if_player_is_getting_hit(player_state)

                if is_player_blocking and (is_player1_attacking or is_player2_attacking):
                    player_state.set_player_action(PlayerAction.BLOCK)

                if not is_player_getting_hit and not is_player_blocking:
                    player_state.set_is_getting_weak_hit(True)
                    player_state.set_player_action(PlayerAction.WEAK_HIT)
                    player_state.reset_animation_attributes()
                    player_state.decrease_health(damage)

                player_attacking_previous_x, _ = player_state.get_player_position()
                is_player_getting_hit_facing_right: bool = player_state.get_is_facing_right()
                new_player_getting_hit_position: float = player_attacking_previous_x + self._hit_speed
                if is_player_getting_hit_facing_right:
                    new_player_getting_hit_position = player_attacking_previous_x - self._hit_speed
                if not is_player_blocking:
                    player_state.set_player_position_x(new_player_getting_hit_position)
        else:
            self._player1_state.set_is_getting_weak_hit(False)
            self._player1_state.set_is_blocking(False)
            self._player2_state.set_is_getting_weak_hit(False)
            self._player2_state.set_is_blocking(False)

    def _change_hit_speed(self, attack_name: str):
        if 'WEAK' in attack_name:
            self._hit_speed = 2
        elif 'MEDIUM' in attack_name:
            self._hit_speed = 4
        elif 'HIGH' in attack_name:
            self._hit_speed = 6

    @staticmethod
    def _detect_if_player_is_getting_hit(player_state: PlayerState) -> bool:
        is_player_getting_hit: bool = (player_state.get_is_getting_weak_hit() or
                                       player_state.get_is_getting_medium_hit() or
                                       player_state.get_is_getting_high_hit())
        return is_player_getting_hit

    def _detect_body_collision(self, player1_body_rect: Rect, player2_body_rect: Rect):
        if player1_body_rect.colliderect(player2_body_rect):
            player1_previous_position_x, _ = self._player1_state.get_player_position()
            player2_previous_position_x, _ = self._player2_state.get_player_position()

            new_player1_position_x: float = player1_previous_position_x - 4
            new_player2_position_x: float = player2_previous_position_x + 4
            is_player1_facing_right: bool = self._player1_state.get_is_facing_right()

            if not is_player1_facing_right:
                new_player1_position_x = player1_previous_position_x + 4
                new_player2_position_x = player2_previous_position_x - 4

            self._player1_state.set_player_position_x(new_player1_position_x)
            self._player2_state.set_player_position_x(new_player2_position_x)

    @staticmethod
    def get_players_collision(player1_body_rect: Rect, player2_body_rect: Rect) -> bool:
        is_players_colliding: bool = False
        if player1_body_rect.colliderect(player2_body_rect):
            is_players_colliding = True
        return is_players_colliding
