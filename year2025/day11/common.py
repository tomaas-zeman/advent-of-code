from networkx import DiGraph, Graph


def parse_input(data: list[str]) -> Graph:
    graph = DiGraph()

    for line in data:
        source = line.split(": ")[0]
        destinations = line.split(": ")[1].split(" ")
        for dest in destinations:
            graph.add_edge(source, dest)

    return graph
