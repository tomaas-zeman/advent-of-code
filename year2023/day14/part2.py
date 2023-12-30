import numpy as np

from year2023.day14.common import compute_result, parse, tilt

CYCLES = 1_000_000_000


def run(data: list[str], is_test: bool):
    grid = parse(data)

    states = {}
    cycle = 0
    while cycle < CYCLES:
        for _ in range(4):
            tilt(grid)
            grid = np.rot90(grid, k=1, axes=(1, 0))
        cycle += 1

        state = tuple(grid.flatten())
        if state in states:
            cycle = CYCLES - ((CYCLES - cycle) % (cycle - states[state]))
        states[state] = cycle

    return compute_result(grid)
