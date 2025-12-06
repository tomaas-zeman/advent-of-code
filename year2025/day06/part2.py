from aocutils import raw_input
from year2025.day06.common import parse_input


def number_extractor(values: list[list[str]]):
    numbers = []

    for i in range(1, len(values[0]) + 1):
        digits = [value[-i] for value in values]
        numbers.append(int("".join(digits)))

    return numbers


@raw_input
def run(data: list[str], is_test: bool):
    tasks = parse_input(data, number_extractor)
    return sum(task.reduce() for task in tasks)


test_result = 3263827
