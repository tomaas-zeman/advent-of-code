from year2022.day16.common import find_flows


def run(data: list[str], is_test: bool):
    return max(find_flows(data, 30).values())


test_result = 1651
