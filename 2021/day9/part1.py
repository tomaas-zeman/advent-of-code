from day9.common import get_data, find_low_points


def run():
    return sum([p.value + 1 for p in find_low_points(get_data())])
