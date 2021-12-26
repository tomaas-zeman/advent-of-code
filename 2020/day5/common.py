from functools import reduce
from math import ceil
from typing import List, Tuple


class Seat:
    def __init__(self, row: int, column: int):
        self.row = row
        self.column = column
        self.id = row * 8 + column


def parse_seats(data: List[str]):
    def reduce_rows(boundaries: Tuple[int, int], instruction: str) -> Tuple[int, int]:
        [lower, upper] = boundaries
        if instruction == 'F':
            return lower, lower + (upper - lower) // 2
        if instruction == 'B':
            return lower + ceil((upper - lower) / 2), upper

    def reduce_cols(boundaries: Tuple[int, int], instruction: str) -> Tuple[int, int]:
        [lower, upper] = boundaries
        if instruction == 'L':
            return lower, lower + (upper - lower) // 2
        if instruction == 'R':
            return lower + ceil((upper - lower) / 2), upper

    return [
        Seat(reduce(reduce_rows, line[0:7], (0, 127))[0], reduce(reduce_cols, line[7:10], (0, 7))[0])
        for line in data
    ]
