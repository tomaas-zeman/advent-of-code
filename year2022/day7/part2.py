from typing import List
from year2022.day7.common import parse_input, Type


def run(data: List[str], raw_data: List[str]):
    [root, all_nodes] = parse_input(data)
    need_to_free = root.size_of_child_nodes - 40000000
    return min(
        [
            n.size_of_child_nodes
            for n in all_nodes
            if n.type == Type.DIRECTORY and n.size_of_child_nodes >= need_to_free
        ]
    )
