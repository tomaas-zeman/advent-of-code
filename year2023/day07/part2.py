from year2023.day07.common import calculate_winnings, parse_hands


def run(data: list[str], is_test: bool):
    hands = parse_hands(data, enable_jokers=True)
    return calculate_winnings(hands)
