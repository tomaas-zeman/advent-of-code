import numpy as np

from common.utils import flatten


def parse_input(data: list[str]):
    valley = np.empty((len(data), len(data[0])), dtype=np.dtype("U100"))
    for row_index, row in enumerate(data):
        for col_index, col in enumerate(row):
            valley[row_index][col_index] = col
    return valley


def next_state(valley: np.ndarray):
    change = {">": (0, 1), "<": (0, -1), "^": (-1, 0), "v": (1, 0)}

    def get_next_position(position, change):
        def sanitize(value, max_value):
            if value > max_value - 2:
                return 1
            if value < 1:
                return max_value - 2
            return value

        row = sanitize(position[0] + change[0], valley.shape[0])
        col = sanitize(position[1] + change[1], valley.shape[1])
        return row, col

    next = np.empty(valley.shape, dtype=np.dtype("U100"))
    for row_index, row in enumerate(valley):
        for col_index, col in enumerate(row):
            for value in col:
                if value in [".", "#", "E", ""]:
                    if next[row_index][col_index]:
                        continue
                    next[row_index][col_index] = value
                else:
                    if not next[row_index][col_index]:
                        next[row_index][col_index] = "."
                    current_next_value = next[get_next_position((row_index, col_index), change[value])]
                    next[get_next_position((row_index, col_index), change[value])] = current_next_value + value

    return next


def next_expedition_positions(valley: np.ndarray, exp: tuple[int, int]):
    return [
        (row, col)
        for row, col in [(exp[0] + 1, exp[1]), (exp[0], exp[1] + 1), (exp[0] - 1, exp[1]), (exp[0], exp[1] - 1), exp]
        if row < valley.shape[0] and row >= 0 and valley[row][col] == "."
    ]


def find_path(start: tuple[int, int], end: tuple[int, int], valley: np.ndarray):
    minutes = 0
    expeditions = set([start])

    while True:
        valley = next_state(valley)
        expeditions = set(flatten([next_expedition_positions(valley, exp) for exp in expeditions]))
        minutes += 1

        for exp in expeditions:
            if exp == end:
                return minutes, valley
