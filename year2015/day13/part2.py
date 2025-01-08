from year2015.day13.common import compute_hapiness, parse


def run(data: list[str], is_test: bool):
    seating = parse(data)
    return compute_hapiness(seating, True)
