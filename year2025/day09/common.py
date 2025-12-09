from aocutils import Point, as_ints


def parse_input(data: list[str]) -> list[Point]:
    points = []
    for line in data:
        points.append(as_ints(line.split(",")))
    return points


def area(p1: Point, p2: Point):
    return abs(p1[0] - p2[0] + 1) * abs(p1[1] - p2[1] + 1)
