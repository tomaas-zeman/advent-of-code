from itertools import permutations


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


def find_longest_path_length(distances: dict[tuple[str, str], int], cities: set[str]):
    longest_distance = 0

    paths = permutations(cities, len(cities))
    for path in paths:
        distance = sum([distances[(path[i], path[i + 1])] for i in range(len(path) - 1)])
        if distance > longest_distance:
            longest_distance = distance

    return longest_distance


def find_shortest_path_length(distances: dict[tuple[str, str], int], cities: set[str]):
    shortest_distance = float("inf")

    paths = permutations(cities, len(cities))
    for path in paths:
        distance = sum([distances[(path[i], path[i + 1])] for i in range(len(path) - 1)])
        if distance < shortest_distance:
            shortest_distance = distance

    return shortest_distance
