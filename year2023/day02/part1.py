from year2023.day02.common import parse_games


def run(data: list[str], is_test: bool):
    games = parse_games(data)
    return sum([g.id for g in games if g.blue <= 14 and g.red <= 12 and g.green <= 13])
