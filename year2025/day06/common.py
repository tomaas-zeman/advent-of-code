from functools import reduce
from operator import add, mul
from typing import Callable


class Task:
    def __init__(self, numbers: list[int], op):
        self.numbers = numbers
        self.op = op

    def reduce(self):
        op = add
        default_value = 0

        if self.op == "*":
            op = mul
            default_value = 1

        return reduce(lambda x, y: op(x, y), self.numbers, default_value)


def empty_array(length: int):
    return [[] for _ in range(length - 1)]


def parse_input(
    data: list[str], number_extractor: Callable[[list[list[str]]], list[int]]
) -> list[Task]:
    tasks: list[Task] = []

    skip_next_col = False
    strings: list[list[str]] = empty_array(len(data))

    for col_idx in range(len(data[0]) - 2, -1, -1):
        if skip_next_col:
            skip_next_col = False
            continue

        for row_idx, row in enumerate(data[:-1]):
            strings[row_idx].insert(0, row[col_idx])

        op = data[-1][col_idx]
        if op in "*+":
            numbers = number_extractor(strings)
            tasks.append(Task(numbers, op))

            strings = empty_array(len(data))
            skip_next_col = True

    return tasks
