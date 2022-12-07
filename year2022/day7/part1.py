from typing import List
from year2022.day7.common import parse_input, Type


def run(data: List[str], raw_data: List[str]):
    return sum(
        [
            node.size_of_child_nodes
            for node in parse_input(data)[1]
            if node.type == Type.DIRECTORY and node.size_of_child_nodes <= 100000
        ]
    )
