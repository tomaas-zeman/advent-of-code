from year2023.day05.common import Map, parse
from functools import reduce
import multiprocessing


def calculate_min_dest(interval_with_maps: tuple[tuple[int, int], list[Map]]):
    interval, maps = interval_with_maps
    min_dest = float('inf')
   
    for j in range(interval[0], interval[1]):
        dest = reduce(lambda dest, map: map.get_dest(dest), maps, j)
        min_dest = min(min_dest, dest)

    return min_dest


# Not necessary but improves parallelism
def split_large_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    max_interval_size = 10_000_000
    smaller_intervals = []
    for interval in intervals:
        for i in range(interval[0], interval[1], max_interval_size):
            smaller_intervals.append((i, min(interval[1], i + max_interval_size)))
    return smaller_intervals


def run(data: list[str], is_test: bool):
    seeds, maps = parse(data)

    intervals = [(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)]
    intervals_with_maps = [(interval, maps) for interval in split_large_intervals(intervals)]

    with multiprocessing.Pool(processes=2 if is_test else 6) as pool:
        results = pool.map(calculate_min_dest, intervals_with_maps)
        return min(results)
