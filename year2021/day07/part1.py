from year2021.day07.common import parse, count_lowest_cost


def run(data: list[str], is_test: bool):
    return count_lowest_cost(parse(data), lambda x, y: abs(x - y))
