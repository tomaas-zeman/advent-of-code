from year2025.day09.common import area, parse_input


def run(data: list[str], is_test: bool):
    points = parse_input(data)

    max_area = 0

    for p1 in points:
        for p2 in [p for p in points if p != p1]:
            max_area = max(max_area, area(p1, p2))

    return max_area


test_result = 50
