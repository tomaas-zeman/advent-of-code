from typing import Callable

from shapely import get_interior_ring
from shapely.geometry import Polygon
from shapely.ops import unary_union

change = {
    "R": (1, 0),
    "L": (-1, 0),
    "D": (0, -1),
    "U": (0, 1),
}


def bounds(polygon: Polygon):
    xs = [x for x, _ in polygon.exterior.coords]
    ys = [y for _, y in polygon.exterior.coords]
    return {
        "min_x": min(xs),
        "max_x": max(xs),
        "min_y": min(ys),
        "max_y": max(ys),
    }


def create_bridge_polygon(last_polygon_coords, new_polygon_coords):
    a = Polygon(last_polygon_coords)
    b = Polygon(new_polygon_coords)

    if a.centroid.x == b.centroid.x:
        ba, bb = (bounds(a), bounds(b)) if a.centroid.y > b.centroid.y else (bounds(b), bounds(a))
        return Polygon(
            [
                (ba["min_x"], ba["min_y"]),
                (ba["max_x"], ba["min_y"]),
                (bb["max_x"], bb["max_y"]),
                (bb["min_x"], bb["max_y"]),
            ]
        )

    ba, bb = (bounds(b), bounds(a)) if a.centroid.x > b.centroid.x else (bounds(a), bounds(b))
    return Polygon(
        [
            (bb["max_x"], bb["min_y"]),
            (bb["max_x"], bb["max_y"]),
            (ba["min_x"], ba["max_y"]),
            (ba["min_x"], ba["min_y"]),
        ]
    )


def get_area(data: list[str], line_parser: Callable[[str], tuple[str, int]]) -> int:
    polygons = [Polygon([(0, 0), (1, 0), (1, 1), (0, 1)])]

    for line in data:
        direction, length = line_parser(line)

        diff_x = change[direction][0] * length
        diff_y = change[direction][1] * length

        last_polygon_coords = [(x, y) for x, y in polygons[-1].exterior.coords]
        new_polygon_coords = [(x + diff_x, y + diff_y) for x, y in last_polygon_coords]

        polygons.append(create_bridge_polygon(last_polygon_coords, new_polygon_coords))
        polygons.append(Polygon(new_polygon_coords))

    shape = unary_union(polygons)
    return int(shape.area + Polygon(get_interior_ring(shape, 0)).area)
