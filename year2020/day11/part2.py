from common.matrix import matrix_from_data, Point


def find_neighbor(seat: Point, delta_row: int, delta_col: int):
    matrix = seat.matrix
    if matrix is None:
        return None

    step = 1
    while 0 <= seat.row + delta_row * step < matrix.num_rows and 0 <= seat.column + delta_col * step < matrix.num_cols:
        neighbor = matrix.point_at_safe(seat.row + delta_row * step, seat.column + delta_col * step)
        if neighbor is not None and neighbor.value != ".":
            return neighbor
        step += 1
    return None


def find_neighbors(seat: Point):
    return [
        n
        for n in [
            find_neighbor(seat, 0, 1),
            find_neighbor(seat, 0, -1),
            find_neighbor(seat, 1, 0),
            find_neighbor(seat, -1, 0),
            find_neighbor(seat, 1, 1),
            find_neighbor(seat, -1, -1),
            find_neighbor(seat, 1, -1),
            find_neighbor(seat, -1, 1),
        ]
        if n is not None
    ]


def run(data: list[str], is_test: bool):
    matrix = matrix_from_data(data)
    while True:
        changes: dict[tuple[int, int], str] = {}

        for seat in matrix.all_points():
            if seat.value == ".":
                continue

            occupied_neighbors = len([n for n in find_neighbors(seat) if n.value == "#"])
            if seat.value == "L" and occupied_neighbors == 0:
                changes[(seat.row, seat.column)] = "#"
            elif seat.value == "#" and occupied_neighbors >= 5:
                changes[(seat.row, seat.column)] = "L"

        # apply changes - everything has to happen at once
        if len(changes) == 0:
            break

        for [row, column], new_value in changes.items():
            point = matrix.point_at_safe(row, column)
            if point:
                point.value = new_value

    return len([point for point in matrix.all_points() if point.value == "#"])
