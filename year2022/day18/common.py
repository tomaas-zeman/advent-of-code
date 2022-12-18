import matplotlib.pyplot as plt
import numpy as np
from typing import Callable

from common.lists import as_ints


def plot(matrix: np.ndarray, x: int, y: int, z: int, filename: str):
    axes = [x, y, z]
    plot = plt.figure()
    axes = plot.add_subplot(111, projection="3d")
    axes.voxels(matrix, facecolors=[1, 0, 0, 0.5])
    plot.savefig(f"year2022/day18/{filename}")
    plot.show()


def calc_surface_area(data: list[str], matrix_postprocess: Callable[[np.ndarray], np.ndarray | None] = lambda a: a):
    max_x = max([int(line.split(",")[0]) for line in data])
    max_y = max([int(line.split(",")[1]) for line in data])
    max_z = max([int(line.split(",")[2]) for line in data])

    matrix = np.zeros((max_x + 1, max_y + 1, max_z + 1))

    for [x, y, z] in [as_ints(line.split(",")) for line in data]:
        matrix[(x, y, z)] = 1

    matrix = matrix_postprocess(matrix)

    if matrix is None:
        raise ValueError("Unexpected calc error - postprocessing failed")

    # plot(matrix, max_x, max_y, max_z, "visualization.png")

    diffs = [np.diff(matrix, 1, axis, 0, 0) for axis in [0, 1, 2]]
    return sum([np.count_nonzero(diff) for diff in diffs])
