from year2020.day5.common import parse_seats


def run(data: list[str], raw_data: list[str]):
    return max([seat.id for seat in parse_seats(data)])
