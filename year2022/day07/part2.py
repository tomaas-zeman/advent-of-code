from year2022.day07.common import parse_input, Type


def run(data: list[str], raw_data: list[str], is_test: bool):
    [root, all_nodes] = parse_input(data)
    need_to_free = root.size_of_child_nodes - 40000000
    return min(
        [n.size_of_child_nodes for n in all_nodes if n.type == Type.DIRECTORY and n.size_of_child_nodes >= need_to_free]
    )
