from enum import Enum
from itertools import permutations
from operator import gt, lt


class PathType(Enum):
    SHORTEST = lt
    LONGEST = gt


def parse_input(data: list[str]) -> tuple[dict[tuple[str, str], int], set[str]]:
    distances = {}
    all_cities = set()

    for line in data:
        [cities, distance] = line.split("=")
        [source, destination] = cities.split(" to ")
        distances[(source.strip(), destination.strip())] = int(distance.strip())
        distances[(destination.strip(), source.strip())] = int(distance.strip())
        all_cities.add(source.strip())
        all_cities.add(destination.strip())

    return distances, all_cities


def find_path_length(distances: dict[tuple[str, str], int], cities: set[str], type: PathType):
    distance = 0 if type == PathType.LONGEST else float('inf')

    paths = permutations(cities, len(cities))
    for path in paths:
        new_distance = sum([distances[(path[i], path[i + 1])] for i in range(len(path) - 1)])
        if type.value(new_distance, distance):
            distance = new_distance

    return distance
