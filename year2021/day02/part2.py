from year2021.day02.common import parse


def run(data: list[str], is_test: bool):
    horizontal_change = 0
    vertical_change = 0
    aim = 0
    for direction, value in parse(data):
        if direction == "forward":
            horizontal_change += value
            vertical_change += aim * value
        elif direction == "up":
            aim -= value
        elif direction == "down":
            aim += value

    return horizontal_change * vertical_change
