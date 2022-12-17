from common.lists import flatten
from year2022.day15.common import parse_input, to_polygons
from shapely.ops import unary_union
from shapely.geometry import LineString


def run(data: list[str], raw_data: list[str], is_test: bool):
    y = 10 if is_test else 2_000_000

    pairs = parse_input(data)
    coords_x = flatten([[p.sensor.x - p.range, p.sensor.x + p.range] for p in pairs])
    line = LineString([(min(coords_x), y), (max(coords_x), y)])
    intersection: LineString = line.intersection(unary_union(to_polygons(pairs)))

    return round(intersection.length)
