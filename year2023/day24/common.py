from __future__ import annotations
from sympy.geometry.line import LinearEntity
from common.utils import Coord


class Hailstone:
    def __init__(self, id: int, position: tuple[int, int, int], velocity: tuple[int, int, int]):
        self.id = id
        self._position = position
        self.velocity = velocity

    def position(self, time: int):
        change = tuple([n * time for n in list(self.velocity)])
        return Coord.add(self._position, change)


def parse(data: list[str]) -> list[Hailstone]:
    return [
        Hailstone(id, tuple(int(n) for n in position.split(", ")), tuple(int(n) for n in velocity.split(", ")))
        for id, (position, velocity) in enumerate(l.split(" @ ") for l in data)
    ]


def intersects_within_range(intersections: list[LinearEntity], range: tuple[int, int]):
    if len(intersections) == 0:
        return False
    return range[0] <= float(intersections[0][0]) <= range[1] and range[0] <= float(intersections[0][1]) <= range[1]
