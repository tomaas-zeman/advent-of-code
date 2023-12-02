import re

from common.utils import as_ints


class Game:
    def __init__(self, id: int, red: int, green: int, blue: int) -> None:
        self.id = id
        self.red = red
        self.green = green
        self.blue = blue


def cube_count(color, turn):
    result = re.findall(f"(\d+) {color}", turn)
    return max(as_ints(result)) if len(result) > 0 else 0


def parse_games(data: list[str]) -> list[Game]:
    games = []

    for line in data:
        id, turns = re.findall("Game (\d+): (.*)", line)[0]
        games.append(Game(int(id), cube_count("red", turns), cube_count("green", turns), cube_count("blue", turns)))

    return games
