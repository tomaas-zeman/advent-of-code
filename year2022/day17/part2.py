import numpy as np

from year2022.day17.common import CAVE_TOP_BUFFER, CAVE_WIDTH, get_tower_size, prototypes, resize_cave, \
    row_of_tower_top, settle_rock

ROCKS = 1_000_000_000_000


def run(data: list[str], is_test: bool):
    cave = resize_cave(np.ones((1, CAVE_WIDTH), dtype=np.int8), CAVE_TOP_BUFFER)

    patterns = set()
    state = None
    additional_tower_height = 0

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
                if pattern in patterns and (state is None or state["pattern"] == pattern):
                    if state is None:
                        state = {
                            "tower_size": get_tower_size(cave),
                            "rock_index": rock_index,
                            "pattern": pattern
                        }
                    else:
                        rock_diff = rock_index - state["rock_index"]
                        tower_size_diff = get_tower_size(cave) - state["tower_size"]
                        remaining_full_cycles = (ROCKS - (state["rock_index"] + 1)) // rock_diff - 1
                        additional_tower_height = remaining_full_cycles * tower_size_diff
                        rock_index += remaining_full_cycles * rock_diff
                elif state is None:
                    patterns.add(pattern)

                break
        
        rock_index += 1

    return get_tower_size(cave) + additional_tower_height


test_result = 1514285714288
