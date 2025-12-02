from aocutils import as_ints
from year2023.day06.common import compute


def run(data: list[str], is_test: bool):
    times = as_ints(data[0].split(":")[1].split())
    records = as_ints(data[1].split(":")[1].split())
    return compute(zip(times, records))


test_result = 288
