from functools import reduce

from year2020.day20.common import parse, find_common_edges


def run(data: list[str], is_test: bool):
    tiles = parse(data)
    common_edges = find_common_edges(tiles)
    return reduce(lambda acc, id: acc * id, [id for id in common_edges.keys() if len(common_edges[id]) == 2])


test_result = 20899048083289
