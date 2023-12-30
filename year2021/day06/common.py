from aocutils import as_ints


def parse(data: list[str]):
    return as_ints(data[0].split(","))
