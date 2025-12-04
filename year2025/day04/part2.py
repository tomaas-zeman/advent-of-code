from year2025.day04.common import create_warehouse, find_accessible_rolls


def run(data: list[str], is_test: bool):
    warehouse = create_warehouse(data)

    total_removed_rolls = 0

    while True:
        accessible_rolls = find_accessible_rolls(warehouse)
        total_removed_rolls += len(accessible_rolls)

        for point in accessible_rolls:
            warehouse[point] = "."

        if len(accessible_rolls) == 0:
            break

        accessible_rolls = []

    return total_removed_rolls


test_result = 43
