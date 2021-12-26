from common.matrix import matrix_from_file


def add_flashing_capability(octopuses):
    for oct in octopuses:
        oct.flashed = False


def reset_flashing(octopuses):
    for oct in octopuses:
        if oct.flashed:
            oct.flashed = False
            oct.value = 0


def flash(octopus):
    for neighbour in octopus.neighbours(diagonals=True):
        neighbour.value += 1


def get_data():
    return matrix_from_file('year2021/day11/data')
