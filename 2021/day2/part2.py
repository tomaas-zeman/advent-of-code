from day2.common import get_data


def run():
    horizontal_change = 0
    vertical_change = 0
    aim = 0
    for direction, value in get_data():
        if direction == 'forward':
            horizontal_change += value
            vertical_change += aim * value
        elif direction == 'up':
            aim -= value
        elif direction == 'down':
            aim += value

    return horizontal_change * vertical_change
