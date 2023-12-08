from year2023.day08.common import parse


def run(data: list[str], is_test: bool):
    instructions, mapping = parse(data)

    current_node = "AAA"
    step = 0
    while True:
        index = step % len(instructions)
        direction = instructions[index]
        current_node = mapping[current_node][direction]
        step += 1

        if current_node == "ZZZ":
            return step
