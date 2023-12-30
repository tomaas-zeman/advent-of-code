from year2021.day04.common import parse


def run(data: list[str], is_test: bool):
    [numbers, boards] = parse(data)

    for number in numbers or []:
        boards = [board for board in boards if not board.has_bingo()]
        for board in boards:
            board.select_number(number)

            if board.has_bingo() and len(boards) == 1:
                return board.sum_remaining_numbers() * number
