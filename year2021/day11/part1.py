from year2021.day11.common import add_flashing_capability, flash, reset_flashing, parse


def run(data: list[str], is_test: bool):
    matrix = parse(data)
    octopuses = matrix.all_points()
    add_flashing_capability(octopuses)

    total_flashes = 0
    for step in range(100):
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
                    total_flashes += 1

            if all([oct.value < 10 or oct.flashed for oct in octopuses]):
                keep_flashing = False

    return total_flashes
