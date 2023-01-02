from __future__ import annotations
import networkx as nx
import re
import matplotlib.pyplot as plt
from itertools import permutations
import time


class Valve:
    def __init__(self, id: str, flow_rate: int, next_valve_ids: list[str]):
        self.id = id
        self.flow_rate = flow_rate
        self.next_valve_ids = next_valve_ids
        self.next_valves: list[Valve] = []

    def __eq__(self, other: Valve):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)


def remap_by_id(valves: list[Valve]):
    valves_by_id = {n.id: n for n in valves}
    for n in valves:
        n.next_valves = [valves_by_id[id] for id in n.next_valve_ids]
    return valves_by_id


def parse_input(data: list[str]):
    pattern = re.compile("Valve ([A-Z]+) has flow rate=(\d+); tunnels? leads? to valves? ([A-Z, ]+)")
    return remap_by_id(
        [Valve(m[1], int(m[2]), [n.strip() for n in m[3].split(",")]) for line in data if (m := pattern.match(line))]
    )


def print_graph(graph: nx.Graph):
    nx.draw(graph, nx.spring_layout(graph, seed=1), with_labels=True)
    plt.show()


def run(data: list[str], is_test: bool):
    graph = nx.Graph()
    valves = parse_input(data)

    for valve in valves.values():
        for next_valve in valve.next_valves:
            graph.add_edge(valve.id, next_valve.id)

    distances = nx.floyd_warshall(graph)
    valid_valves = [valve for valve in valves.values() if valve.flow_rate > 0]

    # TODO: can't really work with full permutations -> too many -> have to skip them continually
    # TODO: try to generate the permutations recursively + memoize all the stuff -> dynamic programming, duh!
    flows = {}
    for permutation in permutations(valid_valves):
        permutation = [valves["AA"]] + list(permutation)
        time_left = 30
        flow = 0

        for i in range(len(permutation)):
            try:
                [src, dest] = permutation[i : i + 2]
            except ValueError:
                src = permutation[i]
                dest = None

            if src.flow_rate > 0:
                time_left -= 1
                flow += src.flow_rate * time_left

            if dest is not None:
                time_left -= distances[src.id][dest.id]
            else:
                flows[flow] = permutation

            if time_left <= 0:
                break

    return int(max(flows.keys()))
