import re
import numpy as np

from aocutils import as_ints


def run(data: list[str], is_test: bool):
    grid = np.zeros((1000, 1000))

    for line in data:
        row_from, col_from, row_to, col_to = as_ints(re.findall("\\d+", line))

        for row in range(row_from, row_to + 1):
            for col in range(col_from, col_to + 1):
                if "toggle" in line:
                    grid[row, col] += 2
                elif "off" in line:
                    grid[row, col] = max(0, grid[row, col] - 1)
                else:
                    grid[row, col] += 1

    return int(np.sum(grid))
