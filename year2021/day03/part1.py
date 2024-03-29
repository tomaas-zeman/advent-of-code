from year2021.day03.common import parse


def run(data: list[str], is_test: bool):
    counter = None
    for bits in parse(data):
        if counter is None:
            counter = [0 for x in range(0, len(bits))]

        for index, value in enumerate(bits):
            counter[index] += 1 if value == 1 else -1

    gamma = ["1" if bit > 0 else "0" for bit in counter]
    epsilon = ["0" if bit > 0 else "1" for bit in counter]

    return int("".join(gamma), 2) * int("".join(epsilon), 2)
