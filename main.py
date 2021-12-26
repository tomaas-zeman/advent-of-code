import traceback
from importlib import import_module
from sys import argv

#
# Expected format of input params
# [0] : <absolute file path>
# [1] : dir=<file dir relative to root>
# [2] : use_test_data=<True|False>
#
[year, day] = argv[1].split('=')[1].split('/')
use_test_data = argv[2].split('=')[1] == 'true'

for part in [1, 2]:
    input_file = f'{year}/{day}/{"testdata" if use_test_data else "data"}'
    with open(input_file, 'r') as file:
        data = [line.strip() for line in file.readlines()]
        try:
            module = f'{year}.{day}.part{part}'
            if '2021' in year:
                result = import_module(module).run()  # does not support autoparse
            else:
                result = import_module(module).run(data)
        except Exception:
            result = 'N/A'
            print(traceback.format_exc())
        print(f'{year} | {day} | part{part:02d} => {result}')
