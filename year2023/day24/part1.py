from itertools import combinations

import sympy.geometry as sg

from year2023.day24.common import intersects_within_range, parse


def run(data: list[str], is_test: bool):
    hailstones = parse(data)
    test_range = (7, 27) if is_test else (200000000000000, 400000000000000)

    intersections = 0
    for h1, h2 in combinations(hailstones, 2):
        line1 = sg.Ray(sg.Point(h1.position(0)[0:2]), sg.Point(h1.position(1)[0:2]))
        line2 = sg.Ray(sg.Point(h2.position(0)[0:2]), sg.Point(h2.position(1)[0:2]))
        if intersects_within_range(line1.intersection(line2), test_range):
            intersections += 1

    return intersections


test_result = 2
