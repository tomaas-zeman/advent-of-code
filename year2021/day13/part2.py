from year2021.day13.common import fold_matrix, get_data, pretty_print


def run():
    matrix = fold_matrix(get_data(), False)
    pretty_print(matrix)
    return None


# # # # . # # # . . # # # # . # . . # . # # # . . # # # # . . . # # . # . . . .
# . . . . # . . # . # . . . . # . # . . # . . # . # . . . . . . . # . # . . . .
# # # . . # . . # . # # # . . # # . . . # # # . . # # # . . . . . # . # . . . .
# . . . . # # # . . # . . . . # . # . . # . . # . # . . . . . . . # . # . . . .
# . . . . # . . . . # . . . . # . # . . # . . # . # . . . . # . . # . # . . . .
# . . . . # . . . . # # # # . # . . # . # # # . . # # # # . . # # . . # # # # .
