import re
from itertools import pairwise

import networkx as nx

from year2023.day23.common import create_graph


def run(data: list[str], is_test: bool):
    graph, start, end = create_graph([re.sub("[<>^v]", ".", line) for line in data], nx.Graph)

    max_length = 0
    for path in nx.all_simple_paths(graph, start, end):
        max_length = max(max_length, sum(graph.get_edge_data(src, dst)["weight"] for src, dst in pairwise(path)))

    return max_length


test_result = 154
