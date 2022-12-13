from common.graph import bfs
from common.matrix import Matrix, matrix_from_data
from year2022.day12.common import expansion


def clear_point_visits(matrix: Matrix):
    for point in matrix.all_points():
        point.flag = False


def run(data: list[str], raw_data: list[str]):
    matrix = matrix_from_data(data)

    starting_points = []
    ending_point = None

    for point in matrix.all_points():
        if point.value in ["S", "a"]:
            starting_points.append(point)
        if point.value == "E":
            ending_point = point

    if len(starting_points) == 0 or ending_point is None:
        raise ValueError("Path points not detected")

    lengths = []
    for starting_point in starting_points:
        clear_point_visits(matrix)
        path = bfs(starting_point, ending_point, expansion)
        if path is not None:
            lengths.append(len(path.points) - 1)

    return min(lengths)
