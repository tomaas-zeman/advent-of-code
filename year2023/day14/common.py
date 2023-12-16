import numpy as np
from common.utils import Numpy


chars = {c: i for i, c in enumerate("O.#")}


def tilt(grid: np.ndarray):
    for col in range(grid.shape[1]):
        start = 0
        for row in range(grid.shape[0]):
            if grid[row, col] == chars["#"]:
                grid[start : row + 1, col].sort()
                start = row + 1
        grid[start : row + 1, col].sort()


def parse(data: list[str]):
    return Numpy.from_input(data, np.uint8, lambda x: chars[x])


def compute_result(grid: np.ndarray):
    return sum(np.sum(grid[::-1][row, :] == chars["O"]) * (row + 1) for row in range(grid.shape[0]))
