from aocutils.matrix import matrix_from_data


def run(data: list[str], is_test: bool):
    matrix = matrix_from_data(data)

    while True:
        changes: dict[tuple[int, int], str] = {}

        for seat in matrix.all_points():
            if seat.value == ".":
                continue

            occupied_neighbors = len([n for n in seat.neighbors(True) if n.value == "#"])
            if seat.value == "L" and occupied_neighbors == 0:
                changes[(seat.row, seat.column)] = "#"
            elif seat.value == "#" and occupied_neighbors >= 4:
                changes[(seat.row, seat.column)] = "L"

        # apply changes - everything has to happen at once
        if len(changes) == 0:
            break

        for [row, column], new_value in changes.items():
            point = matrix.point_at_safe(row, column)
            if point:
                point.value = new_value

    return len([point for point in matrix.all_points() if point.value == "#"])
