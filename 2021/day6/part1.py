from day6.common import get_data


def run():
    counters = get_data()

    for day in range(0, 80):
        for i in range(0, len(counters)):
            counter = counters[i]

            if counter == 0:
                counters.append(8)
                counters[i] = 6
            else:
                counters[i] -= 1

    return len(counters)
