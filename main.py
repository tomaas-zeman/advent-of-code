import traceback
from importlib import import_module
from sys import argv
from common.console import Color, with_color

#
# Expected format of input params
# [0] : <absolute file path>
# [1] : dir=<file dir relative to root>
#
# Run as: python main.py dir=year2022/day1
#
[year, day] = argv[1].split("=")[1].split("/")


def compute_solution(module: str, part: int, data: list[str], raw_data: list[str]):
    # 2021 does not support autoparse
    if "2021" in year:
        return (import_module(module).run(), None)

    test_solution_prefix = "# part"
    if len(data) > 2 and data[0].startswith(test_solution_prefix) and data[1].startswith(test_solution_prefix):
        expected_test_solution = data[part - 1].split(" = ")[1]
        solution = import_module(module).run(data[2:], raw_data=raw_data[2:])
        return solution, expected_test_solution
    else:
        return (import_module(module).run(data, raw_data=raw_data), None)


def run_with_file(filename: str):
    run_result = True
    for part in [1, 2]:
        input_file = f"{year}/{day}/{filename}"
        expected_test_solution = None
        with open(input_file, "r") as file:
            raw_data = file.readlines()
            data = [line.strip() for line in raw_data]
            try:
                module = f"{year}.{day}.part{part}"
                solution, expected_test_solution = compute_solution(module, part, data, raw_data)
            except Exception:
                solution = "ERR"
                print(traceback.format_exc())
                run_result = False

            color = Color.GREEN
            symbol = "✔"
            if (
                solution is None
                or (expected_test_solution is not None and expected_test_solution != str(solution))
                or solution == "ERR"
            ):
                color = Color.BOLD_RED
                symbol = "✘"
                run_result = False

            print(with_color(f"{symbol} {year} | {day} | part{part:02d} => {solution}", color))
    return run_result


# 2021 does not support testdata
if "2021" in year:
    run_with_file("data")
else:
    print("\nRunning with test data ...\n")
    if run_with_file("testdata"):
        print("\nPASSED. Running with real data ...\n")
        run_with_file("data")
