from year2020.day22.common import compute_result, parse


def create_state(players: list[list[int]]):
    return ",".join([str(i) for i in players[0]]) + ",".join([str(i) for i in players[1]])


def recursive_combat(states: set[str], players):
    while True:
        new_state = create_state(players)

        if new_state in states:
            return 0

        states.add(new_state)

        p1 = players[0].pop()
        p2 = players[1].pop()

        winner, stack = 0 if p1 > p2 else 1, sorted([p1, p2])

        if len(players[0]) >= p1 and len(players[1]) >= p2:
            winner = recursive_combat(set(), [players[0][-p1:], players[1][-p2:]])
            stack = [p2, p1] if winner == 0 else [p1, p2]

        players[winner] = stack + players[winner]

        if any(len(p) == 0 for p in players):
            return 0 if players[0] else 1


def run(data: list[str], is_test: bool):
    players = parse(data)
    recursive_combat(set(), players)
    return compute_result(players)
