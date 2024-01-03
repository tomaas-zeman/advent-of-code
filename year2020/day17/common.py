from __future__ import annotations

from dataclasses import dataclass
from itertools import product

from aocutils import Point, Tuple


def get_neighbor_positions(cube: Point, dimensions: int) -> list[Point]:
    return [
        Tuple.add(cube, diffs) for diffs in product([-1, 0, 1], repeat=dimensions) if diffs != tuple([0] * dimensions)
    ]


@dataclass
class State:
    active_cubes: set[Point]
    dim_ranges: list[int]
    dimensions: int

    def expand(self):
        for i, change in enumerate([-1, 1] * self.dimensions):
            self.dim_ranges[i] += change

    def update(self, deactivate: set[Point], activate: set[Point]):
        self.active_cubes.difference_update(deactivate)
        self.active_cubes.update(activate)


def parse(data: list[str], dimensions: int):
    active_cubes = set()
    for row, row_value in enumerate(data):
        for col, col_value in enumerate(row_value):
            if col_value == "#":
                active_cubes.add(tuple([row, col] + [0] * (dimensions - 2)))
    return active_cubes


def count_active_cubes(data: list[str], dimensions: int):
    state = State(parse(data, dimensions), [0, len(data), 0, len(data[0])] + [0, 1] * (dimensions - 2), dimensions)

    for step in range(6):
        state.expand()
        deactivate = set()
        activate = set()

        for cube in product(*[list(range(*state.dim_ranges[i : i + 2])) for i in range(0, len(state.dim_ranges), 2)]):
            active_neighbors = len([n for n in get_neighbor_positions(cube, dimensions) if n in state.active_cubes])

            if cube in state.active_cubes and active_neighbors not in [2, 3]:
                deactivate.add(cube)
            elif cube not in state.active_cubes and active_neighbors == 3:
                activate.add(cube)

        state.update(deactivate, activate)

    return len(state.active_cubes)
