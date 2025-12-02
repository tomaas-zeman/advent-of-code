from year2023.day18.common import get_area


def line_parser(line: str) -> tuple[str, int]:
    code = line.split("#")[1]
    direction = {"0": "R", "1": "D", "2": "L", "3": "U"}[code[-2:-1]]
    return direction, int(code[:5], 16)


def run(data: list[str], is_test: bool):
    return get_area(data, line_parser)


test_result = 952408144115
