from operator import add

from aocutils import as_ints


def run(data: list[str], is_test: bool):
    sum = 0
    for line in data:
        a, b, c = as_ints(line.split("x"))
        sum += 2 * add(*sorted([a, b, c])[0:2]) + a * b * c
    return sum
