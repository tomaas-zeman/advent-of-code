import re
from functools import reduce
from itertools import combinations
from typing import Callable

import networkx as nx


def solve(graph: nx.Graph, generate_edge_combinations: Callable[[nx.Graph], list[list[tuple[str, str]]]]):
    for edges_to_remove in generate_edge_combinations(graph):
        [graph.remove_edge(src, dst) for src, dst in edges_to_remove]
        components = list(nx.connected_components(graph))

        if len(components) > 1:
            return reduce(lambda acc, comp: acc * len(comp), components, 1)
        else:
            [graph.add_edge(src, dst) for src, dst in edges_to_remove]


def run(data: list[str], is_test: bool):
    graph = nx.Graph()

    for source, destinations in [
        (m.group(1), m.group(2).split(" ")) for line in data if (m := re.match(r"(\w+): ([\w ]+)", line))
    ]:
        graph.add_nodes_from([source] + destinations)
        for destination in destinations:
            graph.add_edge(source, destination)

    if is_test:
        # Slow and complete solution
        return solve(graph, lambda g: combinations(g.edges, 3))

    # Quick solution based on visualisation: Graph.draw(graph)
    return solve(graph, lambda _: [[("xnn", "txf"), ("nhg", "jjn"), ("tmc", "lms")]])
