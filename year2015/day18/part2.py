import numpy as np
from aocutils import Numpy


def run(data: list[str], is_test: bool):
    steps = 5 if is_test else 100
    grid = Numpy.from_input_as_str(data)

    grid[0, 0] = "#"
    grid[0, -1] = "#"
    grid[-1, 0] = "#"
    grid[-1, -1] = "#"

    for _ in range(steps):
        clone = np.copy(grid)

        for row in range(grid.shape[0]):
            for col in range(grid.shape[1]):
                ns = Numpy.neighbors_of((row, col), grid, True)
                ns_on = len([n for n in ns if n == "#"])
                if (
                    (row == 0 and col == 0)
                    or (row == 0 and col == grid.shape[1] - 1)
                    or (row == grid.shape[0] - 1 and col == 0)
                    or (row == grid.shape[0] - 1 and col == grid.shape[1] - 1)
                ):
                    continue
                if grid[row, col] == "#":
                    clone[row, col] = "#" if 2 <= ns_on <= 3 else "."
                else:
                    clone[row, col] = "#" if ns_on == 3 else "."

        grid = clone

    return np.count_nonzero(grid == "#")
