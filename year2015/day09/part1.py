from year2015.day09.common import parse_input, find_shortest_path_length


def run(data: list[str], is_test: bool):
    [distances, cities] = parse_input(data)
    return find_shortest_path_length(distances, cities)
