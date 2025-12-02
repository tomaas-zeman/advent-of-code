import networkx as nx

from year2023.day23.common import create_graph


# Essentially running a topological sort algorithm
def run(data: list[str], is_test: bool):
    graph, _, _ = create_graph(data, nx.DiGraph)
    return nx.dag_longest_path_length(graph)


test_result = 94
