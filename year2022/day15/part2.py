from shapely.geometry import Polygon, Point
from shapely.ops import unary_union, clip_by_rect

from year2022.day15.common import parse_input, to_polygons


def run(data: list[str], is_test: bool):
    pairs = parse_input(data)
    shape: Polygon = clip_by_rect(unary_union(to_polygons(pairs)), 0, 0, 4_000_000, 4_000_000)

    # interiors: finds area inside of the polygon that's empty
    # e.g. LINEARRING (13 11, 14 10, 15 11, 14 12, 13 11)
    #
    # and that area surrounds the point we look for
    free_point: Point = shape.interiors[0].centroid

    # round for floating point error (e.g. 56000011.00000001 -> 56000011)
    return round(4_000_000 * free_point.x + free_point.y)
