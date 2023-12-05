from year2023.day05.common import parse
from functools import reduce


def run(data: list[str], is_test: bool):
    seeds, maps = parse(data)
    return min([reduce(lambda dest, map: map.get_dest(dest), maps, seed) for seed in seeds])
