from typing import List, Dict


def path_to_com_from(planet: str, orbits: Dict[str, str]):
    path = []
    next = orbits.get(planet, None)

    while next is not None:
        path.append(next)
        next = orbits.get(next, None)

    return path


def construct_orbits(data: List[str]) -> Dict[str, str]:
    orbits = {}

    for line in data:
        [planet, orbitee] = line.split(")")
        orbits[orbitee] = planet

    return orbits
