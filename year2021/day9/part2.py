from collections import deque
from functools import reduce

from year2021.day9.common import get_data, find_low_points


def get_basin_size(low_point, grid):
    points = set([low_point])

    stack = deque([low_point])
    while len(stack) > 0:
        current_point = stack.pop()
        valid_neighbours = [n for n in grid.neighbours_of(current_point) if n.value < 9]
        for neighbour in valid_neighbours:
            if neighbour not in points:
                points.add(neighbour)
                stack.append(neighbour)

    return len(points)


def run():
    grid = get_data()
    return reduce(
        lambda x, y: x * y,
        sorted([
            get_basin_size(low_point, grid)
            for low_point in find_low_points(grid)
        ])[-3:])
