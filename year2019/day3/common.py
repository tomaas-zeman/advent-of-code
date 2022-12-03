from __future__ import annotations
from enum import Enum
from typing import List


class LineOrientation(Enum):
    HORIZONTAL = 1
    VERTICAL = 2


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def manhattan_dist(self, other: Point) -> int:
        return abs(self.x - other.x) + abs(self.y - other.y)

    def __eq__(self, other: Point) -> bool:
        return self.x == other.x and self.y == other.y

    def __str__(self) -> str:
        return f"[{self.x}:{self.y}]"


class Line:
    def __init__(self, p1: Point, p2: Point) -> None:
        if p1.x < p2.x or p1.y < p2.y:
            self.p1 = p1
            self.p2 = p2
        else:
            self.p1 = p2
            self.p2 = p1

        self.orientation = (
            LineOrientation.VERTICAL if p1.x == p2.x else LineOrientation.HORIZONTAL
        )
        self.last_point = p2

    def find_intersection_point(self, line: Line) -> Point:
        if self.orientation == line.orientation:
            return None

        h = self if self.orientation == LineOrientation.HORIZONTAL else line
        v = self if self.orientation == LineOrientation.VERTICAL else line

        if (
            v.p1.x in list(range(h.p1.x, h.p2.x))
            and h.p1.y in list(range(v.p1.y, v.p2.y))
            and h.p1.x != 0
            and v.p1.x != 0
        ):
            return Point(v.p1.x, h.p1.y)

        return None

    def common_point(self, line: Line) -> Point:
        for point1 in [self.p1, self.p2]:
            for point2 in [line.p1, line.p2]:
                if point1 == point2:
                    return point1
        return None

    def __str__(self) -> str:
        return f"{str(self.p1)} -> {str(self.p2)}"


def generate_lines(paths) -> List[Line]:
    lines = []
    last_point = Point(0, 0)

    for path in paths:
        direction = path[0]
        amount = int(path[1:])

        if direction == "L":
            new_point = Point(last_point.x - amount, last_point.y)
        if direction == "R":
            new_point = Point(last_point.x + amount, last_point.y)
        if direction == "D":
            new_point = Point(last_point.x, last_point.y - amount)
        if direction == "U":
            new_point = Point(last_point.x, last_point.y + amount)

        lines.append(Line(last_point, new_point))
        last_point = new_point

    return lines
