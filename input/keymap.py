from enum import Enum
from pygame import (K_d, K_a, K_s, K_w, K_k, K_j, K_u, K_l, K_i, K_o,
                    K_RIGHT, K_LEFT, K_DOWN, K_UP, K_KP4, K_KP5, K_KP6, K_KP7, K_KP8, K_KP9)


class Keymap:
    class Player1(Enum):
        FORWARD = K_d
        BACKWARD = K_a
        CROUCH = K_s
        JUMP = K_w
        WEAK_PUNCH = K_k
        MEDIUM_PUNCH = K_j
        HIGH_PUNCH = K_u
        WEAK_KICK = K_l
        MEDIUM_KICK = K_i
        HIGH_KICK = K_o

    class Player2(Enum):
        FORWARD = K_RIGHT
        BACKWARD = K_LEFT
        CROUCH = K_DOWN
        JUMP = K_UP
        WEAK_PUNCH = K_KP5
        MEDIUM_PUNCH = K_KP4
        HIGH_PUNCH = K_KP7
        WEAK_KICK = K_KP6
        MEDIUM_KICK = K_KP8
        HIGH_KICK = K_KP9


class QuizKeymap:
    class Player1(Enum):
        UP = Keymap.Player1.JUMP.value
        DOWN = Keymap.Player1.CROUCH.value
        CONFIRM_BUTTONS = [
            Keymap.Player1.WEAK_PUNCH.value,
            Keymap.Player1.MEDIUM_PUNCH.value,
            Keymap.Player1.HIGH_PUNCH.value
        ]
        CANCEL_BUTTONS = [
            Keymap.Player1.WEAK_KICK.value,
            Keymap.Player1.MEDIUM_KICK.value,
            Keymap.Player1.HIGH_KICK.value
        ]

    class Player2(Enum):
        CANCEL_BUTTONS = [
            Keymap.Player2.WEAK_KICK.value,
            Keymap.Player2.MEDIUM_KICK.value,
            Keymap.Player2.HIGH_KICK.value
        ]
        CONFIRM_BUTTONS = [
            Keymap.Player2.WEAK_PUNCH.value,
            Keymap.Player2.MEDIUM_PUNCH.value,
            Keymap.Player2.HIGH_PUNCH.value
        ]
        DOWN = Keymap.Player2.CROUCH.value
        UP = Keymap.Player2.JUMP.value
