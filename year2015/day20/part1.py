from year2015.day20.common import find_divisors


def run(data: list[str], is_test: bool):
    threshold = int(data[0])

    for house in range(threshold):
        if sum(d * 10 for d in find_divisors(house)) >= threshold:
            return house


test_result = 8
