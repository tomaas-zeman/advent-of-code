import re
from dataclasses import dataclass

import numpy as np

from aocutils import split_list_by, Numpy


@dataclass
class Tile:
    id: int
    map: np.ndarray

    def variations(self):
        variations = []
        current_map = self.map
        for _ in range(4):
            current_map = np.rot90(current_map)
            variations.append(current_map)
            variations.append(np.fliplr(current_map))
            variations.append(np.flipud(current_map))
        return variations

    def edges(self):
        return [variation[0, :] for variation in self.variations()]


def parse(data: list[str]) -> list[Tile]:
    tiles = []
    for group in split_list_by(data, ""):
        id = re.match(r"Tile (\d+):", group[0]).group(1)
        map = Numpy.from_input_as_str(group[1:])
        tiles.append(Tile(int(id), map))
    return tiles
