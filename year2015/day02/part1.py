from operator import mul

from aocutils import as_ints


def run(data: list[str], is_test: bool):
    sum = 0
    for line in data:
        a, b, c = as_ints(line.split("x"))
        sum += 2 * a * b + 2 * b * c + 2 * a * c + mul(*sorted([a, b, c])[0:2])
    return sum
