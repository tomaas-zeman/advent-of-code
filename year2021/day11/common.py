from aocutils.matrix import matrix_from_data


def add_flashing_capability(octopuses):
    for oct in octopuses:
        oct.flashed = False


def reset_flashing(octopuses):
    for oct in octopuses:
        if oct.flashed:
            oct.flashed = False
            oct.value = 0


def flash(octopus):
    for neighbor in octopus.neighbors(diagonals=True):
        neighbor.value += 1


def parse(data: list[str]):
    return matrix_from_data(data, convert_value=lambda x: int(x))
