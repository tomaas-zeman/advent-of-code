from __future__ import annotations
import numpy as np
from common.utils import Numpy


#
# ^ z
# |
# |   ╱ y
# | ╱
# +---------> x
class Brick:
    def __init__(self, id: int, range_x: tuple[int, int], range_y: tuple[int, int], range_z: tuple[int, int]):
        self.range_x = range_x
        self.range_y = range_y
        self.range_z = range_z
        self.id = id
        self.supported_by: set[Brick] = set()
        self.loaded_by: set[Brick] = set()

    def drop(self):
        self.range_z = (self.range_z[0] - 1, self.range_z[1] - 1)

    def add_supported_by(self, bricks: list[Brick]):
        self.supported_by.update(bricks)
        [b.add_loaded_by(self) for b in bricks]

    def add_loaded_by(self, brick: Brick):
        self.loaded_by.add(brick)

    def __str__(self):
        support = f"support: {','.join(str(b.id) for b in self.supported_by)}"
        load = f"load: {','.join(str(b.id) for b in self.loaded_by)}"
        return f"[{str(self.id)}] {support} {load}"


def parse(data: list[str]) -> list[Brick]:
    bricks = []
    for id, line in enumerate(data):
        coords = line.split("~")
        ranges = zip(map(int, coords[0].split(",")), map(int, coords[1].split(",")))
        bricks.append(Brick(id + 1, *ranges))
    return bricks


def plot(bricks: list[Brick]):
    def to_matrix_slice(brick: Brick) -> tuple[slice, slice, slice]:
        return (
            slice(brick.range_x[0], brick.range_x[1] + 1),
            slice(brick.range_y[0], brick.range_y[1] + 1),
            slice(brick.range_z[0], brick.range_z[1] + 1),
        )

    grid = np.full(
        (
            max([max(b.range_x) for b in bricks]) + 1,
            max([max(b.range_y) for b in bricks]) + 1,
            max([max(b.range_z) for b in bricks]) + 1,
        ),
        fill_value=0,
    )

    grid[:, :, 0] = -1

    for brick in bricks:
        grid[to_matrix_slice(brick)] = brick.id

    Numpy.plot_3d_as_cubes(grid)
