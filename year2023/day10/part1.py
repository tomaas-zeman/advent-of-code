from year2023.day10.common import walk_path


def run(data: list[str], is_test: bool):
    _, _, steps = walk_path(data)
    return steps
