from networkx import Graph, all_simple_paths
from year2025.day11.common import parse_input
from networkx.drawing.nx_agraph import to_agraph


def draw(graph: Graph):
    agraph = to_agraph(graph)
    agraph.layout("dot")
    agraph.draw("graph.jpg")


def run(data: list[str], is_test: bool):
    graph = parse_input(data)

    # cutoffs are based on the drawing from `draw(graph)`
    # TODO: if there's time, just change this to dfs() and slap @cache on it
    return (
        len(list(all_simple_paths(graph, "svr", "fft", cutoff=10)))
        * len(list(all_simple_paths(graph, "fft", "dac", cutoff=18)))
        * len(list(all_simple_paths(graph, "dac", "out", cutoff=10)))
    )


test_result = 2
