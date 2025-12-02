from year2023.day09.common import calculate_next_number


def initial_sequence(line: str):
    return [int(x) for x in line.split()][::-1]


def run(data: list[str], is_test: bool):
    return sum(calculate_next_number(initial_sequence(line)) for line in data)


test_result = 2
