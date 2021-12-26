from day6.common import get_data


def rotate(array):
    return array[1:] + array[:1]


def run():
    fish_per_counter = [0 for counter in range(9)]
    for counter in get_data():
        fish_per_counter[counter] += 1

    for day in range(256):
        newborns = fish_per_counter[0]
        fish_per_counter[0] = 0

        fish_per_counter = rotate(fish_per_counter)
        fish_per_counter[8] = newborns
        fish_per_counter[6] += newborns

    return sum(fish_per_counter)
