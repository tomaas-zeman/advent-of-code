from year2022.day21.common import parse_input, recursing_to_madness


def run(data: list[str], is_test: bool):
    return recursing_to_madness(parse_input(data)["root"])
