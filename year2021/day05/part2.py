from year2021.day05.common import parse, get_all_points, create_grid, get_intersection_count


def run(data: list[str], is_test: bool):
    paths = parse(data, True)
    points = get_all_points(paths)
    return get_intersection_count(create_grid(points), points)
