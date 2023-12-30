from year2021.day12.common import find_all_paths, parse


def run(data: list[str], is_test: bool):
    return len(find_all_paths(parse(data)))
