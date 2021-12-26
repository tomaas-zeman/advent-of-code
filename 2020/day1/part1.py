from typing import List
from itertools import combinations


def run(data: List[str]):
    numbers = [int(line) for line in data]
    for [one, two] in combinations(numbers, 2):
        if one + two == 2020:
            return one * two
