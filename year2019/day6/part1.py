from typing import List
from year2019.day6.common import path_to_com_from, construct_orbits


def run(data: List[str]):
    orbits = construct_orbits(data)
    return sum([len(path_to_com_from(planet, orbits)) for planet in orbits.keys()])
