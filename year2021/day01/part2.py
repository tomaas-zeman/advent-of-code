from collections import deque

from year2021.day01.common import get_data


def run():
    increases = 0
    buffer_a = deque([], 3)
    buffer_b = deque([], 3)

    for value in get_data():
        if len(buffer_a) == 0:
            buffer_a.append(value)
            continue

        buffer_b.append(value)

        if len(buffer_a) == 3 and len(buffer_b) == 3 and sum(buffer_b) > sum(buffer_a):
            increases += 1

        buffer_a.append(value)

    return increases
