from day5.common import get_data, get_all_points, create_grid, get_intersection_count


def run():
    paths = get_data(True)
    points = get_all_points(paths)
    return get_intersection_count(create_grid(points), points)
