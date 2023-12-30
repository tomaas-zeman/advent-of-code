from typing import Callable

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation, PillowWriter

from aocutils import as_ints


def plot(before: np.ndarray, after: np.ndarray):
    figure, axes = plt.subplots(1, 2)

    def animate(i):
        axes[0].clear()
        axes[0].set_xlim(0, before.shape[0])
        axes[0].set_ylim(0, before.shape[1])
        axes[0].set_title("Original rock with holes")
        axes[1].clear()
        axes[1].set_xlim(0, after.shape[0])
        axes[1].set_ylim(0, after.shape[1])
        axes[1].set_title("After filling the holes")
        return (
            axes[0].matshow(before.take(i, axis=2)),
            axes[1].matshow(after.take(i, axis=2)),
        )

    animation = FuncAnimation(figure, animate, blit=True, repeat=True, frames=before.shape[2] - 1)
    animation.save(f"year2022/day18/animation.gif", dpi=300, writer=PillowWriter(fps=2))


def calc_surface_area(data: list[str], matrix_postprocess: Callable[[np.ndarray], np.ndarray | None] = lambda a: a):
    max_x = max([int(line.split(",")[0]) for line in data])
    max_y = max([int(line.split(",")[1]) for line in data])
    max_z = max([int(line.split(",")[2]) for line in data])

    matrix = np.zeros((max_x + 1, max_y + 1, max_z + 1))

    for [x, y, z] in [as_ints(line.split(",")) for line in data]:
        matrix[(x, y, z)] = 1

    processed_matrix = matrix_postprocess(matrix)
    if processed_matrix is None:
        raise ValueError("Unexpected calc error - postprocessing failed")

    plot(matrix, processed_matrix)

    diffs = [np.diff(processed_matrix, 1, axis, 0, 0) for axis in [0, 1, 2]]
    return sum([np.count_nonzero(diff) for diff in diffs])
