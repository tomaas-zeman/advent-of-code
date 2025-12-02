from aocutils import Numpy
from year2023.day16.common import Beam, Direction, energized_tiles_count


def run(data: list[str], is_test: bool):
    device = Numpy.from_input_as_str(data)
    return energized_tiles_count(Beam((0, 0), Direction.RIGHT), device)


test_result = 46
