from year2021.day13.common import fold_matrix, get_data


def run():
    matrix = fold_matrix(get_data(), True)
    return len([item for item in matrix.all_points() if item.value])
