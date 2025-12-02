from year2020.day22.common import compute_result, parse


def run(data: list[str], is_test: bool):
    players = parse(data)

    while all(len(p) > 0 for p in players):
        p1 = players[0].pop()
        p2 = players[1].pop()
        winner = 0 if p1 > p2 else 1
        players[winner] = sorted([p1, p2]) + players[winner]

    return compute_result(players)


test_result = 306
