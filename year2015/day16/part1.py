from year2015.day16.common import expected, find_aunt_suzie, parse


def run(data: list[str], is_test: bool):
    if is_test:
        return True
    aunts = parse(data)
    return find_aunt_suzie(aunts, lambda thing, count: expected[thing] == count)
