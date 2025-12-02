from year2023.day15.common import hash


def run(data: list[str], is_test: bool):
    return sum(hash(s) for s in data[0].split(","))


test_result = 1320
