from enum import Enum


class SoundType(Enum):
    WEAK_PUNCH = 0
    MEDIUM_PUNCH = 1
    HIGH_PUNCH = 2
    WEAK_KICK = 3
    MEDIUM_KICK = 4
    HIGH_KICK = 5

    OPTION_CHANGE = 'OPTION_CHANGE'
    SELECTED = 'SELECTED'
