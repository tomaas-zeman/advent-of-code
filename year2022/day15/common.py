from __future__ import annotations
import re
from shapely.geometry import Polygon


class Coord:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


class Pair:
    def __init__(self, sensor: Coord, beacon: Coord) -> None:
        self.sensor = sensor
        self.beacon = beacon
        self.range = abs(sensor.x - beacon.x) + abs(sensor.y - beacon.y)


def parse_input(data: list[str]):
    pattern = re.compile(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)")
    return [
        Pair(Coord(int(match[1]), int(match[2])), Coord(int(match[3]), int(match[4])))
        for line in data
        if (match := pattern.match(line))
    ]


def to_polygons(pairs: list[Pair]):
    return [
        Polygon(
            [
                (p.sensor.x, p.sensor.y + p.range),
                (p.sensor.x + p.range, p.sensor.y),
                (p.sensor.x, p.sensor.y - p.range),
                (p.sensor.x - p.range, p.sensor.y),
            ]
        )
        for p in pairs
    ]
