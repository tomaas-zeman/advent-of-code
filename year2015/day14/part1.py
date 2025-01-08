from year2015.day14.common import max_time, parse, race_progress


def run(data: list[str], is_test: bool):
    reindeers = parse(data)
    time = max_time(is_test)
    distances_each_sec = race_progress(reindeers, time)
    return max(d[time] for d in distances_each_sec)
