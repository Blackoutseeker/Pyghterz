from enum import Enum
from pygame import (K_d, K_a, K_s, K_w, K_k, K_j, K_u, K_l, K_i, K_o, K_RIGHT,
                    K_LEFT, K_DOWN, K_UP, K_4, K_5, K_6, K_7, K_8, K_9)


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
        WEAK_PUNCH = K_5
        MEDIUM_PUNCH = K_4
        HIGH_PUNCH = K_7
        WEAK_KICK = K_6
        MEDIUM_KICK = K_8
        HIGH_KICK = K_9
