from __future__ import annotations

import re
from enum import Enum
from typing import Callable

import numpy as np


class Facing(Enum):
    LEFT = 2
    UP = 3
    RIGHT = 0
    DOWN = 1


COORD_CHANGES = {Facing.LEFT: (0, -1), Facing.RIGHT: (0, 1), Facing.UP: (-1, 0), Facing.DOWN: (1, 0)}


class Me:
    def __init__(
        self,
        row: int,
        col: int,
        facing: Facing,
        find_next_valid_coord: NextCoordCallbackType,
    ) -> None:
        self.row = row
        self.col = col
        self.facing = facing
        self.find_next_valid_coord = find_next_valid_coord

    def move(self, steps: int, maze: np.ndarray):
        for _ in range(steps):
            row, col, facing = self.find_next_valid_coord(self, self.facing, maze)
            if self.row == row and self.col == col:
                break
            else:
                self.row = row
                self.col = col
                self.facing = facing

    def turn(self, direction: str):
        self.facing = Facing((self.facing.value + (1 if direction == "R" else -1)) % 4)


def split_raw_line(line: str):
    return re.split("", line)[1:-2]


def parse_input(data: list[str], find_next_valid_coord: NextCoordCallbackType):
    instructions = filter(None, re.split("(\d+|R|L)", data[-1]))

    cols = max([len(split_raw_line(line)) for line in data[:-1]])
    rows = len(data) - 2
    maze = np.empty((rows, cols), dtype=str)

    me = None

    for row_index, row in enumerate(data[:-1]):
        for col_index, col in enumerate(split_raw_line(row)):
            maze[row_index][col_index] = col
            if col == "." and me is None:
                me = Me(row_index, col_index, Facing.RIGHT, find_next_valid_coord)

    if me is None:
        raise ValueError("Cannot find initial position for myself")

    return maze, instructions, me


def find_password(data: list[str], find_next_valid_coord: NextCoordCallbackType):
    maze, instructions, me = parse_input(data, find_next_valid_coord)

    for inst in instructions:
        if inst in ["L", "R"]:
            me.turn(inst)
        else:
            me.move(int(inst), maze)

    return 1000 * (me.row + 1) + 4 * (me.col + 1) + me.facing.value


NextCoordCallbackType = Callable[[Me, Facing, np.ndarray], tuple[int, int, Facing]]
