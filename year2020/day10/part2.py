from collections import deque, OrderedDict
from typing import List

from common.lists import as_ints


def dfc(D, v, M={}):
    if v in M:
        return M[v]
    elif D[v]:
        M[v] = sum(dfc(D, x, M) for x in D[v])
        return M[v]
    else:
        return 1


def alternative(jolts):
    dag = OrderedDict([(x, {y for y in range(x + 1, x + 4) if y in jolts}) for x in jolts])
    print(f'Verified: {dfc(dag, 0)}')


def slice_data(data, initial_index):
    index = initial_index
    while index < len(data) - 1:
        if data[index + 1] - data[index] == 3:
            return data[initial_index:index + 1]
        index += 1


class Combination:
    def __init__(self, initial_numbers):
        self.numbers = initial_numbers

    def __str__(self):
        return ''.join([str(n) for n in self.numbers])

    def __eq__(self, other):
        return str(self) == str(other)

    def __hash__(self):
        return int(str(self))


def count_arrangements(numbers):
    def next_combinations_for(combination):
        return [
            Combination(combination.numbers + [n])
            for n in numbers if n > combination.numbers[-1] and n - combination.numbers[-1] <= 3
        ]

    if numbers is None:
        return 0, 1

    combinations = set()

    stack = deque([Combination([numbers[0]])])
    while len(stack) > 0:
        current_combination = stack.pop()
        new_combinations = next_combinations_for(current_combination)
        if len(new_combinations) == 0:
            combinations.add(current_combination)
        else:
            stack.extend(new_combinations)

    return len(combinations), len(numbers)


def run(data: List[str], raw_data: List[str]):
    arrangements = 0

    jolts = as_ints(data)
    jolts = sorted([0] + jolts + [jolts[-1] + 3])

    alternative(jolts)

    index = 0
    while index < len(jolts) - 1:
        new_arrangements, index_shift = count_arrangements(slice_data(jolts, index))
        arrangements += new_arrangements
        index += index_shift

    return arrangements
