from year2021.day4.common import get_data


def run():
    [numbers, boards] = get_data()

    for number in numbers or []:
        boards = [board for board in boards if not board.has_bingo()]
        for board in boards:
            board.select_number(number)

            if board.has_bingo() and len(boards) == 1:
                return board.sum_remaining_numbers() * number
