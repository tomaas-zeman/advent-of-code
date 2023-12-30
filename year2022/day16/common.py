from __future__ import annotations

import re
from queue import PriorityQueue

import networkx as nx


class Valve:
    def __init__(self, id: str, flow_rate: int, next_valve_ids: list[str]):
        self.id = id
        self.flow_rate = flow_rate
        self.next_valve_ids = next_valve_ids
        self.next_valves: list[Valve] = []

    def __eq__(self, other: Valve):
        return self.id == other.id

    def __lt__(self, other: Valve):
        return other.flow_rate - self.flow_rate

    def __hash__(self):
        return hash(self.id)


def parse_input(data: list[str]):
    pattern = re.compile(r"Valve ([A-Z]+) has flow rate=(\d+); tunnels? leads? to valves? ([A-Z, ]+)")
    valves = [
        Valve(m[1], int(m[2]), [n.strip() for n in m[3].split(",")]) for line in data if (m := pattern.match(line))
    ]
    valves_by_id = {n.id: n for n in valves}
    for n in valves:
        n.next_valves = [valves_by_id[id] for id in n.next_valve_ids]
    return valves_by_id


def find_flows(data: list[str], time: int):
    graph = nx.Graph()
    valves = parse_input(data)

    for valve in valves.values():
        for next_valve in valve.next_valves:
            graph.add_edge(valve.id, next_valve.id)

    distances = nx.floyd_warshall(graph)
    valid_valves = [valve for valve in valves.values() if valve.flow_rate > 0]
    valve_bits = {valve: bit for bit, valve in enumerate(valid_valves)}
    all_valves_visited = sum([1 << i for i in range(len(valid_valves))])

    max_flows_per_state: dict[int, int] = {}

    paths = PriorityQueue[tuple[int, Valve, int, int, int]]()
    paths.put((0, valves["AA"], 0, time, 0))

    while not paths.empty():
        _, current_valve, visited_valves_bitmap, time_left, flow = paths.get()

        unvisited_valves = [v for v in valid_valves if not visited_valves_bitmap & (1 << valve_bits[v])]
        for next_valve in unvisited_valves:
            # go to valve
            new_time_left = time_left - int(distances[current_valve.id][next_valve.id])

            # open it
            new_time_left = new_time_left - 1
            new_flow = flow + (new_time_left * next_valve.flow_rate)

            # update state and queue it if possible
            new_visited_valves_bitmap = visited_valves_bitmap | (1 << valve_bits[next_valve])

            if (
                new_visited_valves_bitmap not in max_flows_per_state
                or new_flow > max_flows_per_state[new_visited_valves_bitmap]
            ):
                max_flows_per_state[new_visited_valves_bitmap] = new_flow
            else:
                continue

            if new_visited_valves_bitmap == all_valves_visited:
                break

            if new_time_left >= 0:
                paths.put((-new_flow, next_valve, new_visited_valves_bitmap, new_time_left, new_flow))

    return max_flows_per_state
