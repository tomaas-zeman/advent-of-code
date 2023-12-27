from collections import deque
from year2023.day22.common import parse, settle_bricks, Brick


def disintegrate(disintegrated: Brick):
    falling = {disintegrated}
    queue = deque([disintegrated])

    while len(queue) > 0:
        brick = queue.pop()
        for load in brick.loaded_by:
            if load.supported_by.issubset(falling):
                falling.add(load)
                queue.appendleft(load)

    return len(falling) - 1


def run(data: list[str], is_test: bool):
    bricks = parse(data)
    settle_bricks(bricks)
    return sum(disintegrate(brick) for brick in bricks)
