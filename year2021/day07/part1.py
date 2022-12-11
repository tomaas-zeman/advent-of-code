from year2021.day07.common import get_data, count_lowest_cost


def run():
    return count_lowest_cost(get_data(), lambda x, y: abs(x - y))
