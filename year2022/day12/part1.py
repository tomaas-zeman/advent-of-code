from common.graph import bfs
from common.matrix import matrix_from_data
from year2022.day12.common import expansion


def run(data: list[str], raw_data: list[str], is_test: bool):
    matrix = matrix_from_data(data)

    starting_point = None
    ending_point = None

    for point in matrix.all_points():
        if point.value == "S":
            starting_point = point
        if point.value == "E":
            ending_point = point

    if starting_point is None or ending_point is None:
        raise ValueError("Path points not detected")

    path = bfs(starting_point, ending_point, expansion)
    if path is not None:
        return len(path.points) - 1
