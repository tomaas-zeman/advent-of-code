#
# https://adventofcode.com/2021
# - https://adventofcode.com/2021/leaderboard/private/view/1721926
#

from importlib import import_module

# days = range(1, 26)
days = [8]

for day in days:
    for part in [1, 2]:
        try:
            result = import_module(f'day{day}.part{part}').run()
        except Exception as e:
            result = 'N/A'
            raise e
            # print(e)
        print(f'Day {day:02d} | Part {part:02d} => {result}')
