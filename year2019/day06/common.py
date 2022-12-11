def path_to_com_from(planet: str, orbits: dict[str, str]):
    path = []
    next = orbits.get(planet, None)

    while next is not None:
        path.append(next)
        next = orbits.get(next, None)

    return path


def construct_orbits(data: list[str]) -> dict[str, str]:
    orbits = {}

    for line in data:
        [planet, orbitee] = line.split(")")
        orbits[orbitee] = planet

    return orbits
