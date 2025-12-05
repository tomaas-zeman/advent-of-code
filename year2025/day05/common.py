from portion import Interval, closed
from aocutils import as_ints


def parse_input(data: list[str]):
    loading_intervals=True

    interval = Interval()
    ingredients = []

    for line in data:
        if len(line) == 0:
            loading_intervals = False
            continue

        if loading_intervals:
            [left, right] = as_ints(line.split('-'))
            interval |= closed(left, right)
        else:
            ingredients.append(int(line))

    return interval, ingredients