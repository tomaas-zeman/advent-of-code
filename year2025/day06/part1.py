from aocutils import raw_input
from year2025.day06.common import parse_input


@raw_input
def run(data: list[str], is_test: bool):
    tasks = parse_input(data, lambda n: [int("".join(digit).strip()) for digit in n])
    return sum(task.reduce() for task in tasks)


test_result = 4277556
