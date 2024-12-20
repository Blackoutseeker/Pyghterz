from pygame.key import get_pressed
from state import PlayerState
from .keymap import Keymap
from utils import MovementSpeed, PlayerAction
from audio import AudioManager, SoundType


class Movement:
    def __init__(self, player_state: PlayerState, another_player_state: PlayerState, is_second_player: bool = False):
        self._player_state: PlayerState = player_state
        self._another_player_state: PlayerState = another_player_state
        self._move_forward_speed: int = player_state.get_movements_speed()[MovementSpeed.MOVE_FORWARD.name]
        self._move_backward_speed: int = player_state.get_movements_speed()[MovementSpeed.MOVE_BACKWARD.name]
        self._is_first_player: bool = is_second_player
        self._player_key = Keymap.Player1
        if is_second_player:
            self._player_key = Keymap.Player2

    def update(self, round_ended: bool, is_players_colliding: bool,
               is_player_colliding_with_left_wall: bool, is_player_colliding_with_right_wall,
               is_players_colliding_with_wall: bool, audio_mgr: AudioManager):
        if not round_ended:
            keys = get_pressed()
            is_player_attacking: bool = self._player_state.get_is_attacking()
            is_player_getting_hit: bool = (self._player_state.get_is_getting_weak_hit() or
                                           self._player_state.get_is_getting_medium_hit() or
                                           self._player_state.get_is_getting_high_hit())
            is_player_blocking: bool = self._player_state.get_is_blocking()
            is_player_facing_right: bool = self._player_state.get_is_facing_right()
            player_action: PlayerAction = PlayerAction.IDLE
            player_position_x, player_position_y = self._player_state.get_player_position()

            if not is_player_attacking:
                if keys[self._player_key.BACKWARD.value]:
                    if not is_player_attacking and not is_player_getting_hit and is_player_facing_right:
                        self._player_state.set_is_blocking(True)
                        player_action = PlayerAction.BLOCK
                elif keys[self._player_key.FORWARD.value]:
                    if not is_player_attacking and not is_player_getting_hit and not is_player_facing_right:
                        self._player_state.set_is_blocking(True)
                        player_action = PlayerAction.BLOCK

            if not is_player_attacking and not is_player_getting_hit and not is_player_blocking:
                if keys[self._player_key.JUMP.value]:
                    # self._position_y -= speed
                    pass
                elif keys[self._player_key.CROUCH.value]:
                    # self._position_y += speed
                    pass
                elif keys[self._player_key.BACKWARD.value]:
                    speed: int = self._move_backward_speed
                    player_action = PlayerAction.MOVE_BACKWARD
                    if not self._player_state.get_is_facing_right():
                        player_action = PlayerAction.MOVE_FORWARD
                        speed = self._move_forward_speed
                    if is_player_facing_right and is_player_colliding_with_left_wall:
                        if player_action == PlayerAction.MOVE_BACKWARD:
                            speed = 0
                    if is_players_colliding_with_wall:
                        if (is_players_colliding and player_action == PlayerAction.MOVE_FORWARD
                                and not is_player_colliding_with_right_wall):
                            speed = 0
                    player_position_x -= speed
                elif keys[self._player_key.FORWARD.value]:
                    speed: int = self._move_forward_speed
                    player_action = PlayerAction.MOVE_FORWARD
                    if not self._player_state.get_is_facing_right():
                        player_action = PlayerAction.MOVE_BACKWARD
                        speed = self._move_backward_speed
                    another_player_action: PlayerAction = self._another_player_state.get_player_action()
                    if is_players_colliding:
                        if another_player_action == PlayerAction.MOVE_FORWARD:
                            speed = 0
                    if not is_player_facing_right and is_player_colliding_with_right_wall:
                        if player_action == PlayerAction.MOVE_BACKWARD:
                            speed = 0
                    if is_players_colliding_with_wall:
                        if (is_players_colliding and player_action == PlayerAction.MOVE_FORWARD
                                and not is_player_colliding_with_left_wall):
                            speed = 0
                    player_position_x += speed

                elif keys[self._player_key.WEAK_PUNCH.value]:
                    self._player_state.set_is_attacking(True)
                    self._player_state.reset_animation_attributes()
                    player_action = PlayerAction.WEAK_PUNCH
                    audio_mgr.play_character_sound('ryu', SoundType.WEAK_PUNCH)
                elif keys[self._player_key.MEDIUM_PUNCH.value]:
                    self._player_state.set_is_attacking(True)
                    self._player_state.reset_animation_attributes()
                    player_action = PlayerAction.MEDIUM_PUNCH
                    audio_mgr.play_character_sound('ryu', SoundType.MEDIUM_PUNCH)
                elif keys[self._player_key.HIGH_PUNCH.value]:
                    self._player_state.set_is_attacking(True)
                    self._player_state.reset_animation_attributes()
                    player_action = PlayerAction.HIGH_PUNCH
                    audio_mgr.play_character_sound('ryu', SoundType.HIGH_PUNCH)
                elif keys[self._player_key.WEAK_KICK.value]:
                    self._player_state.set_is_attacking(True)
                    self._player_state.reset_animation_attributes()
                    player_action = PlayerAction.WEAK_KICK
                    audio_mgr.play_character_sound('ryu', SoundType.WEAK_KICK)
                elif keys[self._player_key.MEDIUM_KICK.value]:
                    self._player_state.set_is_attacking(True)
                    self._player_state.reset_animation_attributes()
                    player_action = PlayerAction.MEDIUM_KICK
                    audio_mgr.play_character_sound('ryu', SoundType.MEDIUM_PUNCH)
                elif keys[self._player_key.HIGH_KICK.value]:
                    self._player_state.set_is_attacking(True)
                    self._player_state.reset_animation_attributes()
                    player_action = PlayerAction.HIGH_KICK
                    audio_mgr.play_character_sound('ryu', SoundType.HIGH_PUNCH)
                self._player_state.set_player_action(player_action)

            self._player_state.set_player_position_x(player_position_x)
            self._player_state.set_player_position_y(player_position_y)
