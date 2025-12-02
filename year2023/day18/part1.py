from year2023.day18.common import get_area


def line_parser(line: str) -> tuple[str, int]:
    direction, length, _ = line.split(" ")
    return direction, int(length)


def run(data: list[str], is_test: bool):
    return get_area(data, line_parser)


test_result = 62
