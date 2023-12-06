from year2023.day06.common import compute


def run(data: list[str], is_test: bool):
    times = [int(x) for x in data[0].split(":")[1].split()]
    records = [int(x) for x in data[1].split(":")[1].split()]
    return compute([(times[i], records[i]) for i in range(len(times))])
