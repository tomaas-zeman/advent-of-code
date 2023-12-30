from year2021.day13.common import fold_matrix, pretty_print, parse


def run(data: list[str], is_test: bool):
    matrix = fold_matrix(parse(data), False)
    pretty_print(matrix)
    return None


# # # # . # # # . . # # # # . # . . # . # # # . . # # # # . . . # # . # . . . .
# . . . . # . . # . # . . . . # . # . . # . . # . # . . . . . . . # . # . . . .
# # # . . # . . # . # # # . . # # . . . # # # . . # # # . . . . . # . # . . . .
# . . . . # # # . . # . . . . # . # . . # . . # . # . . . . . . . # . # . . . .
# . . . . # . . . . # . . . . # . # . . # . . # . # . . . . # . . # . # . . . .
# . . . . # . . . . # # # # . # . . # . # # # . . # # # # . . # # . . # # # # .
