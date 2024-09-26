from utils import PlayerAction


class PlayerState:
    def __init__(self):
        self._player_action: PlayerAction = PlayerAction.IDLE

    def get_player_action(self) -> PlayerAction:
        return self._player_action

    def set_player_action(self, player_action: PlayerAction):
        self._player_action = player_action
