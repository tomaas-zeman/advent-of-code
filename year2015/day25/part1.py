import re

from aocutils import as_ints


def number_at_position(row: int, col: int):
    diagonal_index = row + col - 1
    starting_diagonal_number = int(((diagonal_index - 1) * diagonal_index) / 2 + 1)
    return starting_diagonal_number + (col - 1)


def run(data: list[str], is_test: bool):
    row, col = as_ints(re.findall("\d+", data[0]))

    code = 20151125
    for _ in range(number_at_position(row, col) - 1):
        code = (code * 252533) % 33554393

    return code


test_result = 27995004
