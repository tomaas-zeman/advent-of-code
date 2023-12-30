from collections import deque

from aocutils import as_ints


def run(data: list[str], is_test: bool):
    increases = 0
    buffer_a = deque([], 3)
    buffer_b = deque([], 3)

    for value in as_ints(data):
        if len(buffer_a) == 0:
            buffer_a.append(value)
            continue

        buffer_b.append(value)

        if len(buffer_a) == 3 and len(buffer_b) == 3 and sum(buffer_b) > sum(buffer_a):
            increases += 1

        buffer_a.append(value)

    return increases
