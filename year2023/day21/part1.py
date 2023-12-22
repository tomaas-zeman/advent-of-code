from common.utils import Numpy
from year2023.day21.common import walk


def run(data: list[str], is_test: bool):
    maze = Numpy.from_input_as_str(data)
    counts = walk(maze, 64)
    return len(counts)
