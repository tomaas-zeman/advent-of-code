from year2015.day10.common import expand


def run(data: list[str], is_test: bool):
    return expand(data, 5 if is_test else 50)


test_result = 6
