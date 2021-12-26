from day1.common import get_data


def run():
    increases = 0
    previous_value = None

    for value in get_data():
        if previous_value is not None and value > previous_value:
            increases += 1
        previous_value = value

    return increases
