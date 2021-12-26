class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def __str__(self):
        return f'[{self.x},{self.y}]'


class Path:
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst

    def path_points(self):
        # diagonal
        if self.src.x != self.dst.x and self.src.y != self.dst.y:
            steps = abs(self.src.x - self.dst.x) + 1
            step_x = -1 if self.src.x > self.dst.x else 1
            step_y = -1 if self.src.y > self.dst.y else 1
            return [self.src] + [
                Point(self.src.x + (step_x * i), self.src.y + (step_y * i))
                for i in range(1, steps)
            ]

        if self.src.x != self.dst.x:
            return [
                Point(new_x, self.src.y)
                for new_x in range(min(self.src.x, self.dst.x),
                                   max(self.src.x, self.dst.x) + 1)
            ]

        if self.src.y != self.dst.y:
            return [
                Point(self.src.x, new_y)
                for new_y in range(min(self.src.y, self.dst.y),
                                   max(self.src.y, self.dst.y) + 1)
            ]


# flatten all the points in all paths
def get_all_points(paths):
    return [
        point for points in [path.path_points() for path in paths]
        for point in points
    ]


def create_grid(points):
    rows = max([point.y for point in points])
    columns = max([point.x for point in points])

    grid = []
    for x in range(0, rows + 1):
        grid.append([])
        for y in range(0, columns + 1):
            grid[x].append(0)

    return grid


def get_intersection_count(grid, points):
    for point in points:
        grid[point.y][point.x] += 1

    intersection_count = 0
    for row in grid:
        for column in row:
            if column > 1:
                intersection_count += 1

    return intersection_count


def get_data(include_diagonals):
    with open('day5/data') as f:
        data = []
        for line in f.readlines():
            [src, dest] = line.strip().split(' -> ')
            [p1x, p1y] = src.split(',')
            [p2x, p2y] = dest.split(',')

            # skip invalid diagonals
            if not include_diagonals and p1x != p2x and p1y != p2y:
                continue

            data.append(Path(Point(p1x, p1y), Point(p2x, p2y)))
        return data
