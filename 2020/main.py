#
# https://adventofcode.com/2020
# - https://adventofcode.com/2020/leaderboard/private/view/1721926
#
import traceback
from importlib import import_module
from sys import argv

days = [10]

for day in days:
    for part in [1, 2]:
        input_file = f'day{day}/{"testdata" if "with_test_data" in argv else "data"}'
        with open(input_file, 'r') as file:
            data = [line.strip() for line in file.readlines()]
            try:
                result = import_module(f'day{day}.part{part}').run(data)
            except Exception:
                result = 'N/A'
                print(traceback.format_exc())
            print(f'Day {day:02d} | Part {part:02d} => {result}')
