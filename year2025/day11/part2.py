from functools import cache
from networkx import Graph
from year2025.day11.common import parse_input
from networkx.drawing.nx_agraph import to_agraph


def draw(graph: Graph):
    agraph = to_agraph(graph)
    agraph.layout("dot")
    agraph.draw("graph.jpg")


def count_paths(graph: Graph, source: str, destination: str):
    @cache
    def dfs(node):
        if node == destination:
            return 1
        return sum([dfs(n) for n in graph.neighbors(node)])

    return dfs(source)


def run(data: list[str], is_test: bool):
    graph = parse_input(data)
    return (
        count_paths(graph, "svr", "fft")
        * count_paths(graph, "fft", "dac")
        * count_paths(graph, "dac", "out")
    )


test_result = 2
