from year2021.day06.common import parse


def run(data: list[str], is_test: bool):
    counters = parse(data)

    for day in range(0, 80):
        for i in range(0, len(counters)):
            counter = counters[i]

            if counter == 0:
                counters.append(8)
                counters[i] = 6
            else:
                counters[i] -= 1

    return len(counters)
