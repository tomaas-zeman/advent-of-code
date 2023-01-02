from common.utils import raw_input
from year2022.day22.common import COORD_CHANGES, Facing, Me, find_password
import numpy as np
from typing import Callable


##############
# TEST SETUP #
##############

TEST_SIZE = 4


def get_test_quadrant(row: int, col: int):
    if row < TEST_SIZE:
        return 1
    if row >= 2 * TEST_SIZE:
        if col >= 3 * TEST_SIZE:
            return 6
        else:
            return 5
    if col < TEST_SIZE:
        return 2
    if col < 2 * TEST_SIZE:
        return 3
    return 4


test_movements: dict[tuple[int, Facing], tuple[int, Facing, Callable[[int, int], tuple[int, int]]]] = {
    (1, Facing.UP): (2, Facing.DOWN, lambda row, col: (TEST_SIZE, col - TEST_SIZE - 1)),
    (1, Facing.LEFT): (3, Facing.DOWN, lambda row, col: (TEST_SIZE, TEST_SIZE + row)),
    (1, Facing.RIGHT): (6, Facing.LEFT, lambda row, col: (3 * TEST_SIZE - row - 1, 4 * TEST_SIZE - 1)),
    (2, Facing.UP): (1, Facing.DOWN, lambda row, col: (0, 3 * TEST_SIZE - col - 1)),
    (2, Facing.DOWN): (5, Facing.UP, lambda row, col: (3 * TEST_SIZE - 1, 3 * TEST_SIZE - col - 1)),
    (2, Facing.LEFT): (6, Facing.UP, lambda row, col: (3 * TEST_SIZE - 1, 5 * TEST_SIZE - row - 1)),
    (3, Facing.UP): (1, Facing.RIGHT, lambda row, col: (col - TEST_SIZE, 2 * TEST_SIZE)),
    (3, Facing.DOWN): (5, Facing.RIGHT, lambda row, col: (4 * TEST_SIZE - col - 1, 2 * TEST_SIZE)),
    (4, Facing.RIGHT): (6, Facing.DOWN, lambda row, col: (2 * TEST_SIZE, 5 * TEST_SIZE - row - 1)),
    (5, Facing.LEFT): (3, Facing.UP, lambda row, col: (3 * TEST_SIZE - 1, 4 * TEST_SIZE - row - 1)),
    (5, Facing.DOWN): (2, Facing.UP, lambda row, col: (2 * TEST_SIZE - 1, 3 * TEST_SIZE - col - 1)),
    (6, Facing.UP): (4, Facing.LEFT, lambda row, col: (5 * TEST_SIZE - col - 1, 4 * TEST_SIZE - 1)),
    (6, Facing.DOWN): (2, Facing.RIGHT, lambda row, col: (5 * TEST_SIZE - col - 1, 0)),
    (6, Facing.RIGHT): (1, Facing.LEFT, lambda row, col: (3 * TEST_SIZE - row - 1, 3 * TEST_SIZE - 1)),
}


##############
# PROD SETUP #
##############

SIZE = 50


def get_quadrant(row: int, col: int):
    if col < SIZE:
        if row < 3 * SIZE:
            return 4
        else:
            return 6
    if col >= 2 * SIZE:
        return 2
    if row < SIZE:
        return 1
    if row < 2 * SIZE:
        return 3
    return 5


movements: dict[tuple[int, Facing], tuple[int, Facing, Callable[[int, int], tuple[int, int]]]] = {
    (1, Facing.UP): (6, Facing.RIGHT, lambda row, col: (2 * SIZE + col, 0)),
    (1, Facing.LEFT): (4, Facing.RIGHT, lambda row, col: (3 * SIZE - row - 1, 0)),
    (2, Facing.UP): (6, Facing.UP, lambda row, col: (4 * SIZE - 1, col - 2 * SIZE)),
    (2, Facing.RIGHT): (5, Facing.LEFT, lambda row, col: (3 * SIZE - row - 1, 2 * SIZE - 1)),
    (2, Facing.DOWN): (3, Facing.LEFT, lambda row, col: (col - SIZE, 2 * SIZE - 1)),
    (3, Facing.LEFT): (4, Facing.DOWN, lambda row, col: (2 * SIZE, row - SIZE)),
    (3, Facing.RIGHT): (2, Facing.UP, lambda row, col: (SIZE - 1, SIZE + row)),
    (4, Facing.UP): (3, Facing.RIGHT, lambda row, col: (SIZE + col, SIZE)),
    (4, Facing.LEFT): (1, Facing.RIGHT, lambda row, col: (3 * SIZE - row - 1, SIZE)),
    (5, Facing.RIGHT): (2, Facing.LEFT, lambda row, col: (3 * SIZE - row - 1, 3 * SIZE - 1)),
    (5, Facing.DOWN): (6, Facing.LEFT, lambda row, col: (2 * SIZE + col, SIZE - 1)),
    (6, Facing.LEFT): (1, Facing.DOWN, lambda row, col: (0, row - 2 * SIZE)),
    (6, Facing.RIGHT): (5, Facing.UP, lambda row, col: (3 * SIZE - 1, row - 2 * SIZE)),
    (6, Facing.DOWN): (2, Facing.DOWN, lambda row, col: (0, 2 * SIZE + col)),
}

config = {
    "movements" : test_movements,
    "quadrant" : get_test_quadrant
}


def find_next_valid_coord(me: Me, facing: Facing, maze: np.ndarray) -> tuple[int, int, Facing]:
    row_change, col_change = COORD_CHANGES[facing]

    row = me.row + row_change
    col = me.col + col_change
    if row < maze.shape[0] and col < maze.shape[1]:
        if maze[row][col] == ".":
            return row, col, facing
        if maze[row][col] == "#":
            return me.row, me.col, facing

    _, facing, get_position = config["movements"][(config["quadrant"](me.row, me.col), facing)]
    row, col = get_position(me.row, me.col)
    if maze[row][col] == ".":
        return row, col, facing

    return me.row, me.col, facing


@raw_input
def run(data: list[str], is_test: bool):
    if not is_test:
        config["movements"] = movements
        config["quadrant"] = get_quadrant
    return find_password(data, find_next_valid_coord)
