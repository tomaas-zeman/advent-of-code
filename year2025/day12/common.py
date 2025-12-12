from dataclasses import dataclass
from aocutils import as_ints, Numpy


@dataclass
class Region:
    width: int
    height: int
    presents: list[int]


def parse_input(data: list[str]) -> list[Region]:
    shapes = []
    regions = []

    i = 0
    while i < len(data):
        if "x" in data[i]:
            width, height = as_ints(data[i].split(":")[0].split("x"))
            presents = as_ints(data[i].split(": ")[1].split(" "))
            regions.append(Region(width, height, presents))
            i += 1
        else:
            shapes.append(
                Numpy.from_input(
                    data[i + 1 : i + 4], int, lambda x: 1 if x == "#" else 0
                )
            )
            i += 5

    return regions
