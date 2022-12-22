from year2022.day22.common import COORD_CHANGES, Facing, Me, find_password
import numpy as np


def find_next_valid_coord(me: Me, facing: Facing, maze: np.ndarray) -> tuple[int, int, Facing]:
    row_change, col_change = COORD_CHANGES[facing]

    step = 1
    while True:
        row = (me.row + row_change * step) % maze.shape[0]
        col = (me.col + col_change * step) % maze.shape[1]
        if maze[row][col] == ".":
            return row, col, facing
        if maze[row][col] == "#":
            return me.row, me.col, facing
        step += 1


def run(data: list[str], raw_data: list[str], is_test: bool):
    return find_password(raw_data, find_next_valid_coord)
