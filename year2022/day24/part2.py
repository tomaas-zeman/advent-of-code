from common.utils import Numpy
from year2022.day24.common import find_path


def run(data: list[str], raw_data: list[str], is_test: bool):
    valley = Numpy.from_input_as_str(data)
    path = [(0, 1), (valley.shape[0] - 1, valley.shape[1] - 2), (0, 1), (valley.shape[0] - 1, valley.shape[1] - 2)]

    total_time = 0
    for i in range(len(path) - 1):
        time, valley = find_path(path[i], path[i + 1], valley)
        total_time += time

    return total_time
