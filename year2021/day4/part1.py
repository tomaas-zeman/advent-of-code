from year2021.day4.common import get_data


def run():
    [numbers, boards] = get_data()

    for number in numbers:
        for board in boards:
            board.select_number(number)
            if board.has_bingo():
                return board.sum_remaining_numbers() * number
