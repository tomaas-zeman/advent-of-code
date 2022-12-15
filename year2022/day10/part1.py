from year2022.day10.common import instructions


def run(data: list[str], raw_data: list[str], is_test: bool):
    value = 1
    step = 0
    information = []

    for line in [line.split(" ") for line in data]:
        instruction = instructions[line[0]]

        for _ in range(instruction.duration):
            step += 1
            if (step - 20) % 40 == 0:
                information.append(int(value * step))

        value = instruction.operation(value, line[1:])

    return sum(information)
