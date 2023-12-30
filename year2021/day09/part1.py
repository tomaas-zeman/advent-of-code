from year2021.day09.common import find_low_points, parse


def run(data: list[str], is_test: bool):
    return sum([p.value + 1 for p in find_low_points(parse(data))])
