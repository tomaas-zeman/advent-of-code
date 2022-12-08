from year2020.day3.common import count_trees_on_path


def run(data: list[str], raw_data: list[str]):
    matrix = [[c for c in row] for row in data]
    return count_trees_on_path(3, 1, matrix)
