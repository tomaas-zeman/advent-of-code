from year2021.day03.common import parse


def find_rating(data, bit, compare):
    ones = [bits for bits in data if bits[bit] == 1]
    zeros = [bits for bits in data if bits[bit] == 0]

    if len(ones) == 1 and len(zeros) == 1:
        return "".join([str(x) for x in (ones if compare(1, 0) else zeros)[0]])

    return find_rating(ones if compare(len(ones), len(zeros)) else zeros, bit + 1, compare)


def run(data: list[str], is_test: bool):
    data = parse(data)
    oxygen_rating = find_rating(data, 0, lambda x, y: x >= y)
    co2_rating = find_rating(data, 0, lambda x, y: x <= y)

    return int(oxygen_rating, 2) * int(co2_rating, 2)
