from year2019.day06.common import path_to_com_from, construct_orbits


def run(data: list[str], is_test: bool):
    orbits = construct_orbits(data)
    return sum([len(path_to_com_from(planet, orbits)) for planet in orbits.keys()])
