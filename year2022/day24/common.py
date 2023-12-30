import numpy as np

from aocutils import Numpy, flatten


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
    for value, row_index, col_index in Numpy.all_items(valley):
        for char in value:
            if char in [".", "#", "E", ""]:
                if next[row_index][col_index]:
                    continue
                next[row_index][col_index] = char
            else:
                if not next[row_index][col_index]:
                    next[row_index][col_index] = "."
                current_next_value = next[get_next_position((row_index, col_index), change[char])]
                next[get_next_position((row_index, col_index), change[char])] = current_next_value + char

    return next


def next_expedition_positions(valley: np.ndarray, exp: tuple[int, int]):
    return [
        (row, col) for row, col in Numpy.valid_neighbor_positions_of(exp, valley) + [exp] if valley[row][col] == "."
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
