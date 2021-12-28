from enum import Enum
from typing import Tuple


class Direction(Enum):
    E = 0
    S = 1
    W = 2
    N = 3


class Rotation(Enum):
    R = 1
    L = -1


def compute_new_position(current_position: Tuple[int, int], direction: Direction, value: int):
    if direction == Direction.E:
        return current_position[0] + value, current_position[1]
    if direction == Direction.S:
        return current_position[0], current_position[1] + value
    if direction == Direction.W:
        return current_position[0] - value, current_position[1]
    if direction == Direction.N:
        return current_position[0], current_position[1] - value