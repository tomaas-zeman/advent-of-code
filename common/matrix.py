from __future__ import annotations


class Point:
    def __init__(self, row: int, column: int, value: int, id: int = None):
        self.row = row
        self.column = column
        self.value = value
        self.id = id

    def neighbours(self, diagonals=False) -> list[Point]:
        return self.matrix.neighbours_of(self, diagonals)

    def __eq__(self, other):
        return self.id == other.id

    def __lt__(self, other):
        return self.id - other.id

    def __hash__(self):
        return hash((self.row, self.column))

    def __str__(self):
        return str(self.value)


class Matrix:
    def __init__(self, rows: list[list[Point]]):
        self.rows = rows
        self.num_rows = len(rows)
        self.num_cols = len(rows[0])
        self.mapped_by_id = {
            point_id: point for point_id, point in
            enumerate(self.all_points())
        }

    def point_by_id(self, point_id: int):
        return self.mapped_by_id[point_id]

    def point_at(self, row: int, column: int):
        if row < 0 or column < 0:
            return None
        try:
            return self.rows[row][column]
        except:
            return None

    def neighbours_of(self, point: Point, diagonals=False) -> list[Point]:
        values = [
            self.point_at(point.row, point.column - 1),
            self.point_at(point.row, point.column + 1),
            self.point_at(point.row - 1, point.column),
            self.point_at(point.row + 1, point.column)
        ]

        if diagonals:
            values = values + [
                self.point_at(point.row - 1, point.column - 1),
                self.point_at(point.row - 1, point.column + 1),
                self.point_at(point.row + 1, point.column - 1),
                self.point_at(point.row + 1, point.column + 1),
            ]

        return [v for v in values if v is not None]

    def all_points(self) -> list[Point]:
        return [column for row in self.rows for column in row]

    def __str__(self):
        return '\n'.join([' '.join([str(p) for p in row]) for row in self.rows])


def matrix_from_file(file_path: str, item_sep=None, convert_value=lambda x: int(x)) -> Matrix:
    with open(file_path) as file:
        rows = []

        for line_index, line in enumerate(file.readlines()):
            line = line.strip()
            items = line if item_sep is None else line.split(item_sep)
            rows.append([
                Point(line_index, item_index, convert_value(item), (line_index * len(items)) + item_index)
                for item_index, item in enumerate(items)
            ])

        matrix = Matrix(rows)

        # add backwards reference to matrix for all points
        for point in matrix.all_points():
            point.matrix = matrix

        return matrix
