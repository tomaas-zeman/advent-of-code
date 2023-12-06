def parse(data: list[str]) -> list[tuple[int, int]]:
    times = [int(x) for x in data[0].split(":")[1].split()]
    records = [int(x) for x in data[1].split(":")[1].split()]
    return [(times[i], records[i]) for i in range(len(times))]


def run(data: list[str], is_test: bool):
    races = parse(data)
    result = 1
    for time, record in races:
        options = 0
        for speed in range(time):
            if speed * (time - speed) > record:
                options += 1
        result *= options
    return result
