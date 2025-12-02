from year2015.day21.common import calculate_cost


def run(data: list[str], is_test: bool):
    return calculate_cost(data, lambda me, _: me.hp <= 0, max, 0)


test_result = 148
