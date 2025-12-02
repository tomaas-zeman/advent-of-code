from year2023.day04.common import parse


def run(data: list[str], is_test: bool):
    cards = parse(data)
    return sum([2 ** (c.winning_card_count - 1) for c in cards if c.winning_card_count > 0])


test_result = 13
