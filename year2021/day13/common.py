from functools import reduce

from common.matrix import Point, Matrix


class Fold:
    def __init__(self, axis, value):
        self.axis = axis
        self.value = value


def pretty_print(matrix):
    print("\n".join([" ".join(["#" if item.value else "." for item in row]) for row in matrix.rows]))


def merge(matrix1, matrix2):
    folded_rows = []
    for row in range(len(matrix1.rows)):
        folded_row = []
        for column in range(len(matrix1.rows[0])):
            value = matrix1.point_at(row, column).value or matrix2.point_at(row, column).value
            folded_row.append(Point(row, column, value))
        folded_rows.append(folded_row)

    return Matrix(folded_rows)


def fold_matrix(data, fold_once=False):
    [matrix, folds] = data

    for fold in folds:
        if fold.axis == "y":
            m1 = Matrix(matrix.rows[0 : fold.value])

            current_m2_rows = matrix.rows[fold.value + 1 : len(matrix.rows)]

            # too tired - hacked correction
            row_diff = m1.num_rows - len(current_m2_rows)
            if row_diff < 0:
                current_m2_rows = current_m2_rows[:row_diff]
            elif row_diff > 0:
                additonal_row = [Point(0, 0, False) for n in range(m1.num_cols)]
                for i in range(row_diff):
                    current_m2_rows.append(additonal_row)

            new_m2_rows = []
            for i in range(fold.value):
                new_m2_rows.append(current_m2_rows[fold.value - (i + 1)])
            m2 = Matrix(new_m2_rows)

            matrix = merge(m1, m2)
        else:
            m1 = Matrix([row[0 : fold.value] for row in matrix.rows])

            current_m2_rows = [row[fold.value + 1 : len(row)] for row in matrix.rows]

            # too tired - hacked correction
            col_diff = m1.num_cols - len(current_m2_rows[0])
            if col_diff < 0:
                current_m2_rows = [row[:col_diff] for row in current_m2_rows]
            elif col_diff > 0:
                additional_cols = [Point(0, 0, False) for n in range(col_diff)]
                current_m2_rows = [row + additional_cols for row in current_m2_rows]

            new_m2_rows = []
            for current_row in current_m2_rows:
                new_m2_row = []
                for i in range(fold.value):
                    new_m2_row.append(current_row[fold.value - (i + 1)])
                new_m2_rows.append(new_m2_row)
            m2 = Matrix(new_m2_rows)

            matrix = merge(m1, m2)
        if fold_once:
            break

    return matrix


def get_data():
    with open("year2021/day13/data") as f:
        folds = []
        points = []

        for line in f.readlines():
            if len(line.strip()) == 0:
                continue

            if line.startswith("fold"):
                [axis, value] = line.strip().replace("fold along ", "").split("=")
                folds.append(Fold(axis, int(value)))
                continue

            [col, row] = line.strip().split(",")
            points.append(Point(int(row), int(col), True))

        num_rows = reduce(max, [point.row for point in points], -1)
        num_cols = reduce(max, [point.column for point in points], -1)

        rows = []
        for row_index in range(num_rows + 1):
            row = []
            for col_index in range(num_cols + 1):
                point = Point(row_index, col_index, 0)
                point.value = point in points
                row.append(point)
            rows.append(row)

        return [Matrix(rows), folds]
