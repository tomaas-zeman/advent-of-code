from __future__ import annotations

import re
from collections import defaultdict
from enum import Enum

from aocutils import Tuple, Point


class Direction(Enum):
    E = "e"
    W = "w"
    NE = "ne"
    NW = "nw"
    SE = "se"
    SW = "sw"

    @classmethod
    def all(cls) -> list[Direction]:
        return [cls.E, cls.W, cls.NE, cls.NW, cls.SE, cls.SW]

    @classmethod
    def from_string(cls, string: str) -> Direction:
        return next(direction for direction in Direction.all() if direction.value == string)


def next_position(position: Point, move: Direction) -> Point:
    change = {
        Direction.W: (-1, 0, 1),
        Direction.E: (1, 0, -1),
        Direction.NW: (0, -1, 1),
        Direction.NE: (1, -1, 0),
        Direction.SW: (-1, 1, 0),
        Direction.SE: (0, 1, -1),
    }
    return Tuple.add(position, change[move])


def get_initial_black_positions(data: list[str]) -> set[Point]:
    tiles: dict[Point, bool] = defaultdict(bool)

    for line in data:
        # https://www.redblobgames.com/grids/hexagons
        # (q, r, s)
        position = (0, 0, 0)
        for move in re.findall(r"(e|w|se|sw|ne|nw)", line):
            position = next_position(position, Direction.from_string(move))

        tiles[position] = not tiles[position]

    return set([position for position, flipped in tiles.items() if flipped is True])
