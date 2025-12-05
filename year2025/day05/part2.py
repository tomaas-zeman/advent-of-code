from year2025.day05.common import parse_input


def run(data: list[str], is_test: bool):
    [interval, _] = parse_input(data)
    return sum([r.upper - r.lower + 1 for r in interval])


test_result = 14