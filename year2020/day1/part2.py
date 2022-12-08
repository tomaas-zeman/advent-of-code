from itertools import combinations


def run(data: list[str], raw_data: list[str]):
    numbers = [int(line) for line in data]
    for [one, two, three] in combinations(numbers, 3):
        if one + two + three == 2020:
            return one * two * three
