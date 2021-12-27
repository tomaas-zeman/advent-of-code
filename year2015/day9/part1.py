from typing import List

from year2015.day9.common import parse_input, find_shortest_path_length


def run(data: List[str]):
    [distances, cities] = parse_input(data)
    return find_shortest_path_length(distances, cities)
