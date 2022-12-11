from math import prod

from year2020.day03.common import count_trees_on_path


def run(data: list[str], raw_data: list[str]):
    matrix = [[c for c in row] for row in data]
    movements = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]
    return prod([count_trees_on_path(right, down, matrix) for right, down in movements])
