from year2020.day05.common import parse_seats


def run(data: list[str], raw_data: list[str], is_test: bool):
    return max([seat.id for seat in parse_seats(data)])
