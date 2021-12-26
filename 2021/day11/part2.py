from day11.common import get_data, add_flashing_capability, flash, reset_flashing


def run():
    matrix = get_data()
    octopuses = matrix.all_points()
    add_flashing_capability(octopuses)

    for step in range(300):
        reset_flashing(octopuses)

        for oct in octopuses:
            oct.value += 1

        keep_flashing = True
        while keep_flashing:
            for oct in octopuses:
                if oct.flashed:
                    continue

                if oct.value >= 10:
                    flash(oct)
                    oct.flashed = True

            if all([oct.value < 10 or oct.flashed for oct in octopuses]):
                keep_flashing = False

        if all([oct.flashed for oct in octopuses]):
            return step + 1
