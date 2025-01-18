from functools import cache
from itertools import product
from year2021.day21.common import Game, parse


@cache
def play(game: Game):
    wins = [0, 0]

    for rolls in product((1, 2, 3), (1, 2, 3), (1, 2, 3)):
        next = game.play_turn(sum(rolls))

        if (winner := next.winner()) is not None:
            wins[winner] += 1
            continue

        res = play(next)
        wins[0] += res[0]
        wins[1] += res[1]

    return wins


def run(data: list[str], is_test: bool):
    return max(play(Game(parse(data), (0, 0), 0, 21)))
