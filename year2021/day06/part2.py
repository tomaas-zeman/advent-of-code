from year2021.day06.common import parse


def rotate(array):
    return array[1:] + array[:1]


def run(data: list[str], is_test: bool):
    fish_per_counter = [0] * 9
    for counter in parse(data):
        fish_per_counter[counter] += 1

    for day in range(256):
        newborns = fish_per_counter[0]
        fish_per_counter[0] = 0

        fish_per_counter = rotate(fish_per_counter)
        fish_per_counter[8] = newborns
        fish_per_counter[6] += newborns

    return sum(fish_per_counter)
