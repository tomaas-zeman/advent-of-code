import numpy as np
from enum import Enum
from common.utils import Numpy


def merge(c1: tuple[int, int], c2: tuple[int, int]) -> tuple[int, int]:
    return (c1[0] + c2[0], c1[1] + c2[1])


class Direction(Enum):
    UP = "1"
    DOWN = "2"
    LEFT = "3"
    RIGHT = "4"


coord_change = {
    Direction.UP: (-1, 0),
    Direction.DOWN: (1, 0),
    Direction.LEFT: (0, -1),
    Direction.RIGHT: (0, 1),
}


class Beam:
    def __init__(self, position: tuple[int, int], direction: Direction) -> None:
        self.position = position
        self.direction = direction


class Empty:
    def next(self, beam: Beam) -> list[Beam]:
        beam.position = merge(beam.position, coord_change[beam.direction])
        return [beam]


class Reflection:
    def __init__(self, mapping):
        self.mapping = mapping

    def next(self, beam: Beam) -> list[Beam]:
        return [
            Beam(merge(beam.position, coord_change[direction]), direction) for direction in self.mapping[beam.direction]
        ]


vertical_splitter_direction_change = {
    Direction.UP: [Direction.UP],
    Direction.DOWN: [Direction.DOWN],
    Direction.LEFT: [Direction.UP, Direction.DOWN],
    Direction.RIGHT: [Direction.UP, Direction.DOWN],
}

horizontal_splitter_direction_change = {
    Direction.LEFT: [Direction.LEFT],
    Direction.RIGHT: [Direction.RIGHT],
    Direction.UP: [Direction.LEFT, Direction.RIGHT],
    Direction.DOWN: [Direction.LEFT, Direction.RIGHT],
}


tldr_mirror_direction_change = {
    Direction.UP: [Direction.LEFT],
    Direction.DOWN: [Direction.RIGHT],
    Direction.LEFT: [Direction.UP],
    Direction.RIGHT: [Direction.DOWN],
}

trdl_mirror_direction_change = {
    Direction.UP: [Direction.RIGHT],
    Direction.DOWN: [Direction.LEFT],
    Direction.LEFT: [Direction.DOWN],
    Direction.RIGHT: [Direction.UP],
}


components = {
    ".": Empty(),
    "|": Reflection(vertical_splitter_direction_change),
    "-": Reflection(horizontal_splitter_direction_change),
    "\\": Reflection(tldr_mirror_direction_change),
    "/": Reflection(trdl_mirror_direction_change),
}


def energized_tiles_count(beam: Beam, device: np.ndarray) -> int:
    stack = [beam]
    visited = np.full(device.shape, "")

    while len(stack) > 0:
        beam = stack.pop()
        visited[beam.position] += beam.direction.value

        for next_beam in components[device[beam.position]].next(beam):
            if (
                Numpy.is_valid_point(next_beam.position, device)
                and next_beam.direction.value not in visited[next_beam.position]
            ):
                stack.append(next_beam)

    return np.count_nonzero(visited)
