import re

SIZE = 5


class Board:
    def __init__(self):
        self.rows: list[list] = []

    def add_row(self, row):
        self.rows.append(row)

    def __str__(self):
        string = ""
        for row in self.rows:
            string += " ".join([str(x) for x in row])
            string += "\n"
        return string

    def select_number(self, number):
        for i in range(0, SIZE):
            for j in range(0, SIZE):
                if self.rows[i][j] == number:
                    self.rows[i][j] = None

    def has_bingo(self):
        # bingo in rows
        for row in self.rows:
            if all([column is None for column in row]):
                return True

        # bingo in columns
        for column in range(0, SIZE):
            if all([row[column] is None for row in self.rows]):
                return True

        return False

    def sum_remaining_numbers(self):
        sum = 0
        for i in range(0, SIZE):
            for j in range(0, SIZE):
                if self.rows[i][j] is not None:
                    sum += self.rows[i][j]
        return sum


def get_data():
    with open("year2021/day04/data") as f:
        numbers = None
        boards = []
        board = Board()
        for line in f.readlines():
            if numbers is None:
                numbers = [int(x) for x in line.strip().split(",")]
                continue

            if len(line.strip()) == 0:
                board = Board()
                boards.append(board)
            else:
                board.add_row([int(x) for x in re.split("[ ]+", line.strip())])

        return numbers, boards
