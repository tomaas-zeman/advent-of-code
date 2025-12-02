from year2023.day11.common import sum_of_shortest_paths


def run(data: list[str], is_test: bool):
    return sum_of_shortest_paths(data, 100 if is_test else 1000000)


test_result = 8410
