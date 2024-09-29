from utils import PlayerAction


class PlayerState:
    def __init__(self):
        self._player_action: PlayerAction = PlayerAction.IDLE
        self._is_attacking: bool = False

    def get_player_action(self) -> PlayerAction:
        return self._player_action

    def set_player_action(self, player_action: PlayerAction):
        self._player_action = player_action

    def get_is_attacking(self) -> bool:
        return self._is_attacking

    def set_is_attacking(self, is_attacking: bool):
        self._is_attacking = is_attacking
