from year2023.day08.common import parse
import math


def run(data: list[str], is_test: bool):
    instructions, mapping = parse(data)

    current_nodes = [key for key in mapping.keys() if key.endswith("A")]
    steps_for_each_path_to_reach_end = [-1] * len(current_nodes)

    step = 0
    while True:
        index = step % len(instructions)
        direction = instructions[index]
        step += 1

        for i, node in enumerate(current_nodes):
            node = mapping[node][direction]
            if node.endswith("Z") and steps_for_each_path_to_reach_end[i] == -1:
                steps_for_each_path_to_reach_end[i] = step
            current_nodes[i] = node

        if all([steps != -1 for steps in steps_for_each_path_to_reach_end]):
            return math.lcm(*steps_for_each_path_to_reach_end)
