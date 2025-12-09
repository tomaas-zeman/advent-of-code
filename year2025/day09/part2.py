from shapely.geometry import Polygon, box
from year2025.day09.common import area, parse_input


def run(data: list[str], is_test: bool):
    points = parse_input(data)
    polygon = Polygon(points)

    max_area = 0

    for p1 in points:
        for p2 in [p for p in points if p != p1]:
            rectangle = box(
                min(p1[0], p2[0]),
                min(p1[1], p2[1]),
                max(p1[0], p2[0]),
                max(p1[1], p2[1]),
            )
            if polygon.contains(rectangle):
                max_area = max(max_area, area(p1, p2))

    return max_area


test_result = 24
