from year2021.day08.common import parse, decode_line_patterns


def run(data: list[str], is_test: bool):
    result = 0
    for patterns, output in parse(data):
        result += int("".join([str(n) for n in decode_line_patterns(patterns, output)]))
    return result
