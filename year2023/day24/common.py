from __future__ import annotations

from sympy import Point2D

from aocutils import Tuple


class Hailstone:
    def __init__(self, id: int, position: tuple[int, ...], velocity: tuple[int, ...]):
        self.id = id
        self._position = position
        self.velocity = velocity

    def position(self, time: int):
        change = tuple([n * time for n in list(self.velocity)])
        return Tuple.add(self._position, change)


def parse(data: list[str]) -> list[Hailstone]:
    return [
        Hailstone(id, tuple(int(n) for n in position.split(", ")), tuple(int(n) for n in velocity.split(", ")))
        for id, (position, velocity) in enumerate(l.split(" @ ") for l in data)
    ]


def intersects_within_range(intersections: list[Point2D], range: tuple[int, int]):
    if len(intersections) == 0:
        return False
    x, y = intersections[0]
    return range[0] <= float(x) <= range[1] and range[0] <= float(y) <= range[1]
