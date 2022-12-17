from __future__ import annotations
import re


def manhattan(c1: Coord, c2: Coord):
    return abs(c1.x - c2.x) + abs(c1.y - c2.y)


def manhattan_perf(c1x: int, c1y: int, c2x: int, c2y: int):
    return abs(c1x - c2x) + abs(c1y - c2y)


class Coord:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


class Pair:
    def __init__(self, sensor: Coord, beacon: Coord) -> None:
        self.sensor = sensor
        self.beacon = beacon
        self.range = manhattan(sensor, beacon)


def parse_input(data: list[str]):
    pattern = re.compile("Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)")
    return [
        Pair(Coord(int(match[1]), int(match[2])), Coord(int(match[3]), int(match[4])))
        for line in data
        if (match := pattern.match(line))
    ]
