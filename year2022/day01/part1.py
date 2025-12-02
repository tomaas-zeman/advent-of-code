from year2022.day01.common import get_elves


def run(data: list[str], is_test: bool):
    return max(get_elves(data))


test_result = 24000
