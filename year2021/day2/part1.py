from year2021.day2.common import get_data


def run():
    horizontal_change = 0
    vertical_change = 0
    for direction, value in get_data():
        if direction == "forward":
            horizontal_change += value
        elif direction == "up":
            vertical_change -= value
        elif direction == "down":
            vertical_change += value

    return horizontal_change * vertical_change
