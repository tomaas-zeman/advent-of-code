from functools import cache
import re
from typing import Callable

from aocutils import as_ints


def vx_change(vx):
    return max(0, vx - 1)


def vy_change(vy):
    return vy - 1


@cache
def position_in_time(velocity: int, time: int, velocity_change: Callable[[int], int]):
    position = 0
    max_position = 0
    for _ in range(time):
        position += velocity
        velocity = velocity_change(velocity)
        max_position = max(max_position, position)
    return position, max_position


def send_probes(data: list[str], is_test: bool) -> tuple[int, set[tuple[int, int]]]:
    [x1, x2, y1, y2] = as_ints(re.findall("(-?\\d+)", data[0]))
    limit = 50 if is_test else 250

    result_max_y = 0
    result_velocities = set()

    for vx in range(1, x2 + 1):
        for vy in range(-limit, limit):
            for t in range(1, limit):
                position_x, _ = position_in_time(vx, t, vx_change)
                position_y, max_y = position_in_time(vy, t, vy_change)

                if x1 <= position_x <= x2 and y1 <= position_y <= y2:
                    result_max_y = max(result_max_y, max_y)
                    result_velocities.add((vx, vy))

    return result_max_y, result_velocities
