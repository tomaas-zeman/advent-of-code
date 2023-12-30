from year2021.day04.common import parse


def run(data: list[str], is_test: bool):
    [numbers, boards] = parse(data)

    for number in numbers or []:
        for board in boards:
            board.select_number(number)
            if board.has_bingo():
                return board.sum_remaining_numbers() * number
