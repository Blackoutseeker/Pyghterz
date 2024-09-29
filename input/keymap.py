from enum import Enum
from pygame import K_d, K_a, K_s, K_w, K_k, K_j, K_u, K_l, K_i, K_o


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
