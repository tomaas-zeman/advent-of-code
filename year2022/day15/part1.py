from common.lists import flatten
from year2022.day15.common import Coord, manhattan, parse_input


def run(data: list[str], raw_data: list[str], is_test: bool):
    y = 10 if is_test else 2_000_000

    pairs = parse_input(data)
    coords_x = flatten([[p.sensor.x - p.range, p.sensor.x + p.range] for p in pairs])
    beacons_with_same_y = len(set([p.beacon.y for p in pairs if p.beacon.y == y]))
    min_x = min(coords_x)
    max_x = max(coords_x)

    occupied_spots = 0
    for x in range(min_x, max_x + 1):
        for pair in pairs:
            if manhattan(Coord(x, y), pair.sensor) <= pair.range:
                occupied_spots += 1
                break

    return occupied_spots - beacons_with_same_y
