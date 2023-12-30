from __future__ import annotations

from enum import Enum


class Type(Enum):
    FILE = 1
    DIRECTORY = 2


class Node:
    def __init__(self, name: str, type: Type, size: int, parent: Node | None = None):
        self.name = name
        self.size = size
        self.parent = parent
        self.type = type
        self.children: list[Node] = []

        self.size_of_child_nodes = 0

    def add_child(self, node: Node):
        self.children.append(node)
        if node.type == Type.FILE:
            Node.add_size_to_parents(self, node.size)

    @staticmethod
    def add_size_to_parents(node: Node, size: int):
        node.size_of_child_nodes += size
        if node.parent is not None:
            Node.add_size_to_parents(node.parent, size)


def parse_input(data: list[str]):
    all_nodes: list[Node] = []
    root = Node("/", Type.DIRECTORY, 0)
    current_node = root

    for line in data[1:]:
        if line.startswith("$ cd"):
            dest = line[5:]
            current_node = (
                (current_node.parent if current_node.parent else root)
                if dest == ".."
                else [c for c in current_node.children if c.name == dest][0]
            )
        if not line.startswith("$"):
            [a, name] = line.split(" ")
            new_node = Node(
                name,
                type=Type.DIRECTORY if a == "dir" else Type.FILE,
                size=0 if a == "dir" else int(a),
                parent=current_node,
            )
            current_node.add_child(new_node)
            all_nodes.append(new_node)

    return root, all_nodes
