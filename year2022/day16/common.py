from __future__ import annotations
from collections import deque
from queue import PriorityQueue
import re

from common.graph import BfsPath


class Node:
    def __init__(self, id: str, flow_rate: int, next_node_ids: list[str]) -> None:
        self.id = id
        self.flow_rate = flow_rate
        self.next_node_ids = next_node_ids
        self.next_nodes = []
        self.pressure_released = False

    def release_pressure(self):
        self.pressure_released = True

    def __eq__(self, other: Node) -> bool:
        return self.id == other.id

    def __hash__(self) -> int:
        return hash(self.id)


class Path(BfsPath[Node]):
    def __init__(self, nodes: list[Node], closed_flow_nodes: set[Node], timer: int = 30, released_pressure: int = 0) -> None:
        super().__init__(nodes)
        self.timer = timer
        self.released_pressure = released_pressure
        self.closed_flow_nodes = closed_flow_nodes

    def copy(self):
        return Path(self.nodes[:], self.closed_flow_nodes, self.timer, self.released_pressure)

    def tick(self):
        self.timer -= 1

    def release_pressure(self, node: Node):
        self.released_pressure += self.timer * node.flow_rate
        node.release_pressure()

    def all_flow_nodes_open(self):
        return len(self.closed_flow_nodes) == 0


def remap_by_id(nodes: list[Node]):
    nodes_by_id = {n.id: n for n in nodes}
    for n in nodes:
        n.next_nodes = [nodes_by_id[id] for id in n.next_node_ids]
    return nodes_by_id


def parse_input(data: list[str]):
    pattern = re.compile("Valve ([A-Z]+) has flow rate=(\d+); tunnels? leads? to valves? ([A-Z, ]+)")
    return remap_by_id(
        [Node(m[1], int(m[2]), [n.strip() for n in m[3].split(",")]) for line in data if (m := pattern.match(line))]
    )


def find_paths(nodes: dict[str, Node]):
    starting_node = nodes["AA"]
    flow_nodes = {n for n in nodes.values() if n.flow_rate > 0}

    paths = []
    queue = deque([Path([starting_node], flow_nodes)])

    while len(queue) > 0:
        path = queue.pop()

        if path.timer <= 0 or path.all_flow_nodes_open():
            paths.append(path)
            continue

        for node in [n for n in path.nodes[-1].next_nodes]:
            new_path = path.copy()
            if node not in new_path.nodes:
                new_path.release_pressure(node)
                new_path.tick()
            new_path.add_node(node)
            new_path.tick()
            queue.append(new_path)

    return paths
