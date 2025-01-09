from year2015.day20.common import find_divisors


def run(data: list[str], is_test: bool):
    threshold = int(data[0])

    for house in range(threshold):
        if sum(d * 11 for d in find_divisors(house) if d * 50 >= house) >= threshold:
            return house
