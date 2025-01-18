from year2021.day21.common import Game, parse


class Die:
    sides = 100
    rolls = 0
    value = 0

    def roll(self):
        next = (self.value + 1) * 3 + 3
        self.value = (self.value + 3) % self.sides
        self.rolls += 3
        return next


def run(data: list[str], is_test: bool):
    die = Die()
    game = Game(parse(data), (0, 0), 0, 1000)

    while game.winner() is None:
        game = game.play_turn(die.roll())

    return min(game.scores) * die.rolls
