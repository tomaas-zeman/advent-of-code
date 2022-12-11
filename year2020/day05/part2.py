from year2020.day05.common import parse_seats


def run(data: list[str], raw_data: list[str]):
    seats = sorted(parse_seats(data), key=lambda seat: seat.id)
    for i in range(1, len(seats)):
        if seats[i + 1].id - seats[i - 1].id != 2:
            return seats[i].id + 1
