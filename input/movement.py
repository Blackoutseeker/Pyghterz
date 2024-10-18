from pygame.key import get_pressed
from state import PlayerState
from .keymap import Keymap
from utils import PlayerAction
from audio import AudioManager, SoundType

speed = 8
audio_manager = AudioManager()


class Movement:
    def __init__(self, player_state: PlayerState, is_second_player: bool = False):
        self._player_state: PlayerState = player_state
        self._is_first_player: bool = is_second_player
        self._player_key = Keymap.Player1
        if is_second_player:
            self._player_key = Keymap.Player2
        self._position_x: float = 80
        if is_second_player:
            self._position_x = 330
        self._position_y: float = 280

    def get_position_x(self) -> float:
        return self._position_x

    def get_position_y(self) -> float:
        return self._position_y

    def update(self, audio_mgr: AudioManager):
        keys = get_pressed()
        is_player_attacking: bool = self._player_state.get_is_attacking()
        player_action: PlayerAction = PlayerAction.IDLE
        if is_player_attacking is False:
            if keys[self._player_key.JUMP.value]:
                # self._position_y -= speed
                pass
            elif keys[self._player_key.CROUCH.value]:
                # self._position_y += speed
                pass
            elif keys[self._player_key.BACKWARD.value]:
                self._position_x -= speed
                player_action = PlayerAction.MOVE_BACKWARD
                if self._player_state.get_is_facing_right() is not True:
                    player_action = PlayerAction.MOVE_FORWARD
            elif keys[self._player_key.FORWARD.value]:
                self._position_x += speed
                player_action = PlayerAction.MOVE_FORWARD
                if self._player_state.get_is_facing_right() is not True:
                    player_action = PlayerAction.MOVE_BACKWARD

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
