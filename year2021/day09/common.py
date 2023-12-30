from aocutils.matrix import matrix_from_data


def find_low_points(grid):
    low_points = []

    for row in range(grid.num_rows):
        for column in range(grid.num_cols):
            point = grid.point_at(row, column)
            if all([adj.value > point.value for adj in grid.neighbors_of(point)]):
                low_points.append(point)

    return low_points


def parse(data: list[str]):
    return matrix_from_data(data, convert_value=lambda x: int(x))
