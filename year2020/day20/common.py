import re
from collections import defaultdict
from dataclasses import dataclass
from itertools import combinations

import numpy as np

from aocutils import split_list_by, Numpy


@dataclass
class Tile:
    id: int
    map: np.ndarray

    def variations(self):
        return generate_variations(self.map)

    def edges(self):
        return [variation[0, :] for variation in self.variations()]


def generate_variations(map: np.ndarray):
    variations = []
    current_map = map
    for _ in range(4):
        current_map = np.rot90(current_map)
        variations.append(current_map)
        variations.append(np.fliplr(current_map))
        variations.append(np.flipud(current_map))
    return variations


def parse(data: list[str]) -> list[Tile]:
    tiles = []
    for group in split_list_by(data, ""):
        id = re.match(r"Tile (\d+):", group[0]).group(1)
        map = Numpy.from_input_as_str(group[1:])
        tiles.append(Tile(int(id), map))
    return tiles


def find_common_edges(tiles: list[Tile]) -> dict[int, list[int]]:
    common_edges = defaultdict(list)

    for t1, t2 in combinations(tiles, 2):
        edges = set(["".join(e) for e in t1.edges()]).intersection(set(["".join(e) for e in t2.edges()]))
        if len(edges) > 0:
            common_edges[t1.id].append(t2.id)
            common_edges[t2.id].append(t1.id)

    return common_edges
