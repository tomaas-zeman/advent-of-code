from common.matrix import Point, Matrix
from common.lists import as_ints, flatten


MATRIX_SIDE_PADDING = 200
MATRIX_BOTTOM_PADDING = 2


class Type:
    SAND = "o"
    SAND_SOURCE = "+"
    ROCK = "#"
    AIR = "."


def bounds(data: list[str]):
    points = flatten([line.split(" -> ") for line in data])
    points_x = [int(p.split(",")[0]) for p in points]
    points_y = [int(p.split(",")[1]) for p in points]
    return min(points_x), max(points_x), max(points_y)


def parse_input(data: list[str]):
    # detect space bounds
    left, right, bottom = bounds(data)

    # create matrix
    rows = []
    for row in range(bottom + 1 + MATRIX_BOTTOM_PADDING):
        num_cols = right - left + 1 + 2 * MATRIX_SIDE_PADDING
        rows.append([Point.simples(row, column, Type.AIR) for column in range(num_cols)])
    matrix = Matrix(rows)

    # mark sand source
    sand_source = matrix.point_at(0, 500 - left + MATRIX_SIDE_PADDING)
    sand_source.value = Type.SAND_SOURCE

    # mark rocks
    for line in data:
        points = line.split(" -> ")
        for i in range(len(points) - 1):
            [x1, y1] = as_ints(points[i].split(","))
            [x2, y2] = as_ints(points[i + 1].split(","))
            for row in range(min(y1, y2), max(y1, y2) + 1):
                for column in range(min(x1, x2) - left, max(x1, x2) - left + 1):
                    matrix.point_at(row, column + MATRIX_SIDE_PADDING).value = Type.ROCK

    return matrix, sand_source


def pick_free(matrix: Matrix, point: Point):
    possible_positions = [
        matrix.point_at_safe(point.row + 1, point.column),
        matrix.point_at_safe(point.row + 1, point.column - 1),
        matrix.point_at_safe(point.row + 1, point.column + 1),
    ]
    free = [p for p in possible_positions if p is not None and p.value == Type.AIR]
    if len(free) == 0:
        return point
    return pick_free(matrix, free[0])
