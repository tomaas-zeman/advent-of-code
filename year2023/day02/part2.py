from year2023.day02.common import parse_games


def run(data: list[str], is_test: bool):
    games = parse_games(data)
    return sum([g.red * g.blue * g.green for g in games])


test_result = 2286
