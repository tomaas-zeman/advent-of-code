from aocutils import Numpy
from year2023.day17.common import dijkstra


def run(data: list[str], is_test: bool):
    matrix = Numpy.from_input_as_int(data)
    return dijkstra(matrix, (0, 0), 10, 4)


test_result = 94
