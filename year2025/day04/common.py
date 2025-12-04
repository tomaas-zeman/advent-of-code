from aocutils import ComplexMatrix

ROLL = "@"


def create_warehouse(data: list[str]):
    return ComplexMatrix[str](data, should_store_value=lambda v: v == ROLL)


def find_accessible_rolls(warehouse: ComplexMatrix[str]) -> list[complex]:
    accessible_rolls = []

    for point, value in warehouse.entries():
        if value == ROLL and len([n for _, n in warehouse.neighbors(point) if n == ROLL]) < 4:
            accessible_rolls.append(point)

    return accessible_rolls
