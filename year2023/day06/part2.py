from year2023.day06.common import compute


def run(data: list[str], is_test: bool):
    time = int("".join(data[0].split(":")[1].split()))
    record = int("".join(data[1].split(":")[1].split()))
    return compute([(time, record)])


test_result = 71503
