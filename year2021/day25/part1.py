import numpy as np
from aocutils import Numpy


def next_position(trench: np.ndarray, row: int, col: int) -> tuple[int, int] | None:
    value = trench[row, col]

    if value == ">":
        next_col = (col + 1) % trench.shape[1]
        return None if trench[row, next_col] != "." else (row, next_col)

    if value == "v":
        next_row = (row + 1) % trench.shape[0]
        return None if trench[next_row, col] != "." else (next_row, col)

    return None


def move(trench: np.ndarray, cucumbers: tuple[int, int]):
    for (row, col), (next_row, next_col) in cucumbers:
        trench[next_row, next_col] = trench[row, col]
        trench[row, col] = "."

    return trench


def get_moving_cucumbers(trench: np.ndarray, cucumber: str):
    cucumbers = []

    for row in range(trench.shape[0]):
        for col in range(trench.shape[1]):
            if (
                trench[row, col] == cucumber
                and (next := next_position(trench, row, col)) is not None
            ):
                cucumbers.append(((row, col), next))

    return cucumbers


def run(data: list[str], is_test: bool):
    trench = Numpy.from_input_as_str(data)
    moves = 1

    while True:
        trech_after_move = np.copy(trench)

        for cucumber in [">", "v"]:
            moving_cucumbers = get_moving_cucumbers(trech_after_move, cucumber)
            trech_after_move = move(trech_after_move, moving_cucumbers)

        if (trench == trech_after_move).all():
            return moves

        moves += 1
        trench = trech_after_move


test_result = 58
