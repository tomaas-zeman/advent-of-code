import re

from aocutils import as_ints


Reindeers = list[tuple[int, int, int]]


def max_time(is_test: bool):
    return 1000 if is_test else 2503


def parse(data: list[str]) -> Reindeers:
    reindeers = []

    for line in data:
        speed, fly_time, rest_time = as_ints(re.findall("\d+", line))
        reindeers.append((speed, fly_time, rest_time))

    return reindeers


def race_progress(reindeers: Reindeers, max_time: int) -> list[list[int]]:
    distances_each_sec = [[0] for _ in reindeers]

    for i in range(len(reindeers)):
        speed, fly_time, rest_time = reindeers[i]
        time = 0
        distance = 0

        while time < max_time:
            section_elapsed_time = min(fly_time, max_time - time)

            for t in range(1, section_elapsed_time + 1):
                distances_each_sec[i].append(distance + speed * t)

            distance += speed * section_elapsed_time

            for _ in range(rest_time):
                distances_each_sec[i].append(distance)

            time += section_elapsed_time
            time += rest_time

    return distances_each_sec
