from aocutils import Numpy
from year2023.day16.common import Beam, Direction, energized_tiles_count


def run(data: list[str], is_test: bool):
    device = Numpy.from_input_as_str(data)
    starting_beams = (
        [Beam((0, i), Direction.DOWN) for i in range(device.shape[1])]
        + [Beam((device.shape[0] - 1, i), Direction.UP) for i in range(device.shape[1])]
        + [Beam((i, 0), Direction.RIGHT) for i in range(device.shape[0])]
        + [Beam((i, device.shape[1] - 1), Direction.LEFT) for i in range(device.shape[0])]
    )

    return max([energized_tiles_count(starting_beam, device) for starting_beam in starting_beams])
