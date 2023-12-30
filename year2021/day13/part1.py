from year2021.day13.common import fold_matrix, parse


def run(data: list[str], is_test: bool):
    matrix = fold_matrix(parse(data), True)
    return len([item for item in matrix.all_points() if item.value])
