from enum import Enum

class Status(Enum):
    SUCCESS = 1
    TIMEOUT = 2
    DEAD = 3
    BAD = 4
    