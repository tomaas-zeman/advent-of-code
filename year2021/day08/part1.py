from year2021.day08.common import decode_line_patterns, parse


def run(data: list[str], is_test: bool):
    result = 0
    for patterns, output in parse(data):
        result += len([n for n in decode_line_patterns(patterns, output) if n in [1, 4, 7, 8]])
    return result
