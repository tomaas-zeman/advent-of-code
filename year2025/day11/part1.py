from networkx import all_simple_paths
from year2025.day11.common import parse_input


def run(data: list[str], is_test: bool):
    graph = parse_input(data)
    return len(list(all_simple_paths(graph, "you", "out")))


test_result = 5
