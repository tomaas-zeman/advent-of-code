from year2015.day14.common import max_time, parse, race_progress


def run(data: list[str], is_test: bool):
    reindeers = parse(data)
    time = max_time(is_test)
    distances_each_sec = race_progress(reindeers, time)

    points = [0 for _ in reindeers]

    for sec in range(time):
        max_distance = max(d[sec] for d in distances_each_sec)
        for i in range(len(reindeers)):
            if distances_each_sec[i][sec] == max_distance:
                points[i] += 1

    return max(points) - 1
