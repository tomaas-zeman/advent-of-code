from year2023.day22.common import parse, settle_bricks


def run(data: list[str], is_test: bool):
    bricks = parse(data)
    settle_bricks(bricks)
    return sum(
        1
        for brick in bricks
        if len(brick.loaded_by) == 0 or all(len(above.supported_by) > 1 for above in brick.loaded_by)
    )


test_result = 5
