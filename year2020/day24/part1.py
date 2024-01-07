from year2020.day24.common import get_initial_black_positions


def run(data: list[str], is_test: bool):
    return len(get_initial_black_positions(data))
