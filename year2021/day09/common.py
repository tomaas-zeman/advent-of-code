from common.matrix import matrix_from_file


def find_low_points(grid):
    low_points = []

    for row in range(grid.num_rows):
        for column in range(grid.num_cols):
            point = grid.point_at(row, column)
            if all([adj.value > point.value for adj in grid.neighbors_of(point)]):
                low_points.append(point)

    return low_points


def get_data():
    return matrix_from_file("year2021/day09/data")
