class Map:
    def __init__(self) -> None:
        self.configs = []

    def add_config(self, src: int, dest: int, range: int):
        self.configs.append((src, dest, range))

    def get_dest(self, number: int):
        for src, dest, range in self.configs:
            if src <= number < src + range:
                return dest + (number - src)
        return number


def parse(data: list[str]) -> tuple[list[int], list[Map]]:
    seeds = [int(x) for x in data[0][7:].split()]
    maps = []

    map = Map()
    for line in [l for l in data[2:] if "map" not in l]:
        if len(line) == 0:
            maps.append(map)
            map = Map()
            continue

        [dest, src, range] = [int(x) for x in line.split()]
        map.add_config(src, dest, range)
    maps.append(map)

    return seeds, maps
