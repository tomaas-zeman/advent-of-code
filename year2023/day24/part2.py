import sympy.geometry as sg
from year2023.day24.common import intersects_within_range, parse


def run(data: list[str], is_test: bool):
    hailstones = parse(data)
    test_range = (7, 27) if is_test else (200000000000000, 400000000000000)

    pass