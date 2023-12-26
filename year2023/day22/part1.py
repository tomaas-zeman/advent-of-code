from typing import Union
from year2023.day22.common import parse, Brick
from portion import closed


def sort_by_z(bricks: list[Brick], mode: Union[min, max]) -> list[Brick]:
    return sorted(bricks, key=lambda brick: mode(brick.range_z))


def can_drop(brick: Brick, bricks: list[Brick]):
    if min(brick.range_z) == 1:
        return False

    bricks_under = [
        b
        for b in bricks
        if b.id != brick.id
        and max(b.range_z) == min(brick.range_z) - 1
        and closed(*b.range_x).overlaps(closed(*brick.range_x))
        and closed(*b.range_y).overlaps(closed(*brick.range_y))
    ]

    if len(bricks_under) == 0:
        return True

    brick.add_supported_by(bricks_under)
    return False


def run(data: list[str], is_test: bool):
    bricks = parse(data)

    for step in range(max([max(b.range_z) for b in bricks])):
        dropped_this_step = 0

        for brick in sort_by_z(bricks, min):
            if can_drop(brick, bricks):
                brick.drop()
                dropped_this_step += 1

        if dropped_this_step == 0:
            break

    return sum(
        1
        for brick in bricks
        if len(brick.loaded_by) == 0 or all(len(above.supported_by) > 1 for above in brick.loaded_by)
    )
