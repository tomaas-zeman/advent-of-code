from year2023.day04.common import parse


def run(data: list[str], is_test: bool):
    cards = parse(data)
    winning_cards = [
        result for c in cards if len((result := set(c.winning).intersection(set(c.scratched)))) > 0
    ]
    return sum([2**(len(c) - 1) for c in winning_cards])

