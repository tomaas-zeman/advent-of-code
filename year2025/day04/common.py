import numpy as np

from aocutils import Numpy


def find_accessible_rolls(warehouse: np.ndarray):
    accessible_rolls = []

    for row in range(warehouse.shape[0]):
        for col in range(warehouse.shape[1]):
            neighbors = Numpy.neighbors_of((row, col), warehouse, True)
            if (
                warehouse[row, col] == "@"
                and len([n for n in neighbors if n == "@"]) < 4
            ):
                accessible_rolls.append((row, col))

    return accessible_rolls
