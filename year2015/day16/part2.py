from year2015.day16.common import expected, find_aunt_suzie, parse


def is_valid(thing: str, count: int) -> bool:
    if thing in ["cats", "trees"]:
        return count > expected[thing]
    if thing in ["pomeranians", "goldfish"]:
        return count < expected[thing]
    return expected[thing] == count


def run(data: list[str], is_test: bool):
    if is_test:
        return True
    aunts = parse(data)
    return find_aunt_suzie(aunts, is_valid)


test_result = True
