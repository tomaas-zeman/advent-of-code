from collections import deque
from functools import reduce

from year2021.day09.common import find_low_points, parse


def get_basin_size(low_point, grid):
    points = {low_point}

    stack = deque([low_point])
    while len(stack) > 0:
        current_point = stack.pop()
        valid_neighbors = [n for n in grid.neighbors_of(current_point) if n.value < 9]
        for neighbor in valid_neighbors:
            if neighbor not in points:
                points.add(neighbor)
                stack.append(neighbor)

    return len(points)


def run(data: list[str], is_test: bool):
    grid = parse(data)
    return reduce(
        lambda x, y: x * y, sorted([get_basin_size(low_point, grid) for low_point in find_low_points(grid)])[-3:]
    )
