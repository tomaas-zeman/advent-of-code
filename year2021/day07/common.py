from aocutils import as_ints


def count_lowest_cost(crabs, cost_fn):
    min_cost = None

    for position in range(min(crabs), max(crabs) + 1):
        cost = sum([cost_fn(crab, position) for crab in crabs])
        if min_cost is None or cost < min_cost:
            min_cost = cost

    return min_cost


def parse(data: list[str]):
    return as_ints(data[0].split(","))
