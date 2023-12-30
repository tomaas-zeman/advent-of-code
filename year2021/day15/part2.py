from aocutils.matrix import Point, Matrix
from year2021.day15.common import get_data
from year2021.day15.part1 import compute_risk

data_repeats = 5


def repeated_point(point, repeat, num_cols, num_rows, row_repeat):
    value = (point.value + repeat) % 10
    repeat_addition = (point.value + repeat) // 10
    row_index = point.row + ((repeat * num_rows) if row_repeat else 0)
    column_index = point.column + (0 if row_repeat else (repeat * num_cols))
    return Point(row_index, column_index, value + repeat_addition, point.id)


def run():
    matrix = get_data()
    huge_matrix_rows = []

    # repeat columns
    for row in matrix.rows:
        huge_row = []
        for repeat in range(data_repeats):
            huge_row += [repeated_point(point, repeat, matrix.num_cols, matrix.num_rows, False) for point in row]
        huge_matrix_rows.append(huge_row)

    # repeat rows
    rows_to_repeat = [row for row in huge_matrix_rows]
    for repeat in range(data_repeats - 1):
        huge_matrix_rows += [
            [repeated_point(point, repeat + 1, matrix.num_cols, matrix.num_rows, True) for point in row]
            for row in rows_to_repeat
        ]

    # reindex points
    matrix = Matrix(huge_matrix_rows)
    for point_id, point in enumerate(matrix.all_points()):
        point.id = point_id
    matrix.mapped_by_id = {point_id: point for point_id, point in enumerate(matrix.all_points())}

    return compute_risk(matrix)
