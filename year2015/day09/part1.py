from year2015.day09.common import PathType, find_path_length, parse_input


def run(data: list[str], is_test: bool):
    [distances, cities] = parse_input(data)
    return find_path_length(distances, cities, PathType.SHORTEST)
