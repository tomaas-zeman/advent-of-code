from year2023.day14.common import compute_result, parse, tilt


def run(data: list[str], is_test: bool):
    grid = parse(data)
    tilt(grid)
    return compute_result(grid)


test_result = 136
