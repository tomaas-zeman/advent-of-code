from typing import List

from year2019.day3.common import generate_lines, Point


def run(data: List[str], raw_data: List[str]):
    paths1 = data[0].split(",")
    paths2 = data[1].split(",")

    lines1 = generate_lines(paths1)
    lines2 = generate_lines(paths2)

    intersections: list[Point] = []
    for line1 in lines1:
        for line2 in lines2:
            intersection = line1.find_intersection_point(line2)
            if intersection is not None:
                intersections.append(intersection)

    return sorted([point.manhattan_dist(Point(0, 0)) for point in intersections])[0]
