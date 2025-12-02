import numpy as np

from year2022.day17.common import (
    CAVE_TOP_BUFFER,
    CAVE_WIDTH,
    get_tower_size,
    prototypes,
    resize_cave,
    row_of_tower_top,
    settle_rock,
)

ROCKS = 2022


def run(data: list[str], is_test: bool):
    cave = resize_cave(np.ones((1, CAVE_WIDTH), dtype=np.int8), CAVE_TOP_BUFFER)

    blow_index = 0
    for rock_index in range(ROCKS):
        rock = prototypes[rock_index % len(prototypes)].new()
        cave = resize_cave(cave, CAVE_TOP_BUFFER + rock.height - row_of_tower_top(cave))

        while True:
            direction = data[0][blow_index]
            blow_index = (blow_index + 1) % len(data[0])

            rock.blow(direction, cave)
            if not rock.fall(cave):
                settle_rock(cave, rock)
                break

    return get_tower_size(cave)


test_result = 3068
