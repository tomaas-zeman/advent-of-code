from year2025.day04.common import create_warehouse, find_accessible_rolls


def run(data: list[str], is_test: bool):
    warehouse = create_warehouse(data)
    return len(find_accessible_rolls(warehouse))


test_result = 13
