from aocutils import as_ints


def run(data: list[str], is_test: bool):
    increases = 0
    previous_value = None

    for value in as_ints(data):
        if previous_value is not None and value > previous_value:
            increases += 1
        previous_value = value

    return increases
