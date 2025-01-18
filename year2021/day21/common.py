from dataclasses import dataclass


def parse(data: list[str]):
    return tuple([int(l.split(": ")[1]) for l in data])


@dataclass(eq=True, frozen=True)
class Game:
    positions: tuple[int, int]
    scores: tuple[int, int]
    player: int
    ending_score: int

    def winner(self) -> None | int:
        winner = None
        for player in range(len(self.scores)):
            if self.scores[player] >= self.ending_score:
                winner = player
        return winner

    def play_turn(self, roll: int):
        positions = list(self.positions)
        positions[self.player] = (positions[self.player] + roll) % 10

        scores = list(self.scores)
        scores[self.player] += (
            10 if positions[self.player] == 0 else positions[self.player]
        )

        player = (self.player + 1) % 2

        return Game(tuple(positions), tuple(scores), player, self.ending_score)
