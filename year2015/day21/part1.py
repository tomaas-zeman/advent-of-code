from year2015.day21.common import calculate_cost


def run(data: list[str], is_test: bool):
    return calculate_cost(data, lambda _, boss: boss.hp <= 0, min, float('inf'))


test_result = 78
