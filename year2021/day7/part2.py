from year2021.day7.common import get_data, count_lowest_cost


def run():
    return count_lowest_cost(get_data(), lambda x, y: sum(range(1, abs(x - y) + 1)))
