from year2021.day8.common import get_data, decode_line_patterns


def run():
    data = get_data()

    result = 0
    for patterns, output in data:
        result += len([n for n in decode_line_patterns(patterns, output) if n in [1, 4, 7, 8]])

    return result
