from year2022.day24.common import find_path
from common.utils import Numpy


def run(data: list[str], raw_data: list[str], is_test: bool):
    valley = Numpy.from_input_as_str(data)
    time, _ = find_path((0, 1), (valley.shape[0] - 1, valley.shape[1] - 2), valley)
    return time
