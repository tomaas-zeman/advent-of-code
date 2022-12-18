from year2022.day17.common import CAVE_TOP_BUFFER, CAVE_WIDTH, prototypes, resize_cave, row_of_tower_top, settle_rock
import numpy as np


ROCKS = 1_000_000_000_000


def run(data: list[str], raw_data: list[str], is_test: bool):
    cave = resize_cave(np.ones((1, CAVE_WIDTH), dtype=np.int8), CAVE_TOP_BUFFER)

    prev_tower_size = 0
    prev_rock_index = 0

    additional_tower_height = 0
    pattern_found = False
    patterns = set()
    blow_index = 0
    rock_index = 0
    while rock_index < ROCKS:
        rock = prototypes[rock_index % len(prototypes)].new()
        cave = resize_cave(cave, CAVE_TOP_BUFFER + rock.height - row_of_tower_top(cave))

        while True:
            direction = data[0][blow_index]
            blow_index = (blow_index + 1) % len(data[0])

            rock.blow(direction, cave)
            if not rock.fall(cave):
                settle_rock(cave, rock)

                pattern = f"{blow_index}>{np.array2string(cave[row_of_tower_top(cave):50,])}"
                if pattern in patterns:
                    if not pattern_found:
                        prev_tower_size = cave.shape[0] - row_of_tower_top(cave) - 1
                        prev_rock_index = rock_index
                        pattern_found = True
                        patterns = set([pattern])
                    else:
                        rock_diff = rock_index - prev_rock_index
                        tower_size_diff = cave.shape[0] - row_of_tower_top(cave) - 1 - prev_tower_size

                        remaining_full_cycles = (ROCKS - (prev_rock_index + 1)) // rock_diff
                        additional_tower_height = (remaining_full_cycles - 1) * tower_size_diff
                        rock_index += (remaining_full_cycles - 1) * rock_diff
                elif not pattern_found:
                    patterns.add(pattern)

                break
        
        rock_index += 1

    # -1 for floor
    return cave.shape[0] - row_of_tower_top(cave) - 1 + additional_tower_height
