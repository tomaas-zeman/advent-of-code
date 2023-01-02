from year2022.day07.common import parse_input, Type


def run(data: list[str], is_test: bool):
    return sum(
        [
            node.size_of_child_nodes
            for node in parse_input(data)[1]
            if node.type == Type.DIRECTORY and node.size_of_child_nodes <= 100000
        ]
    )
