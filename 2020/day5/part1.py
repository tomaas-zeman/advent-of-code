from typing import List

from day5.common import parse_seats


def run(data: List[str]):
    return max([seat.id for seat in parse_seats(data)])
