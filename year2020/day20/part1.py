from collections import defaultdict
from functools import reduce
from itertools import combinations

from year2020.day20.common import parse


def run(data: list[str], is_test: bool):
    tiles = parse(data)

    common_edges = defaultdict(list)
    for t1, t2 in combinations(tiles, 2):
        edges = set(["".join(e) for e in t1.edges()]).intersection(set(["".join(e) for e in t2.edges()]))
        if len(edges) > 0:
            common_edges[t1.id].append(t2.id)
            common_edges[t2.id].append(t1.id)

    return reduce(lambda acc, id: acc * id, [id for id in common_edges.keys() if len(common_edges[id]) == 2])
