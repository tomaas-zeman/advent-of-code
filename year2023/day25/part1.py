import re
from itertools import combinations

import networkx as nx


def run(data: list[str], is_test: bool):
    graph = nx.Graph()

    for source, destinations in [
        (m.group(1), m.group(2).split(" ")) for line in data if (m := re.match(r"(\w+): ([\w ]+)", line))
    ]:
        graph.add_nodes_from([source] + destinations)
        for destination in destinations:
            graph.add_edge(source, destination, capacity=1)

    for node1, node2 in combinations(graph.nodes, 2):
        cut_size, partition = nx.minimum_cut(graph, node1, node2)
        if cut_size == 3:
            return len(partition[0]) * len(partition[1])


test_result = 54
