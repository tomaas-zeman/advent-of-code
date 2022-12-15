from year2019.day06.common import path_to_com_from, construct_orbits


def run(data: list[str], raw_data: list[str], is_test: bool):
    orbits = construct_orbits(data)
    you_to_com = path_to_com_from("YOU", orbits)[::-1]
    san_to_com = path_to_com_from("SAN", orbits)[::-1]

    for i in range(min(len(you_to_com), len(san_to_com))):
        if you_to_com[i] != san_to_com[i]:
            return len(you_to_com) + len(san_to_com) - 2 * i
