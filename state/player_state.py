from utils import PlayerAction


class PlayerState:
    def __init__(self):
        self._player_action: PlayerAction = PlayerAction.IDLE
