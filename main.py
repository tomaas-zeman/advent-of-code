import traceback
from importlib import import_module
from sys import argv
from common.utils import measure_time, Console

#
# Expected format of input params
# [0] : <absolute file path>
# [1] : dir=<file dir relative to root>
#
# Run as: python main.py dir=year2022/day1
#
[year, day] = argv[1].split("=")[1].split("/")


@measure_time
def compute_solution(module: str, part: int, data: list[str], raw_data: list[str], is_test: bool):
    # 2021 does not support autoparse
    if "2021" in year:
        return (import_module(module).run(), None)

    test_solution_prefix = "# part"
    if len(data) > 2 and data[0].startswith(test_solution_prefix) and data[1].startswith(test_solution_prefix):
        expected_test_solution = data[part - 1].split(" = ")[1]
        solution = import_module(module).run(data[2:], raw_data=raw_data[2:], is_test=is_test)
        return solution, expected_test_solution
    else:
        return (import_module(module).run(data, raw_data=raw_data, is_test=is_test), None)


def run_with_file(filename: str, part: int):
    run_result = True
    input_file = f"{year}/{day}/{filename}"
    expected_test_solution = None
    with open(input_file, "r") as file:
        raw_data = file.readlines()
        data = [line.strip() for line in raw_data]
        try:
            module = f"{year}.{day}.part{part}"
            solution, expected_test_solution = compute_solution(module, part, data, raw_data, is_test=filename == 'testdata')
        except Exception:
            solution = "ERR"
            print(traceback.format_exc())
            run_result = False

        color = None
        symbol = "✔"
        if (
            solution is None
            or (expected_test_solution is not None and expected_test_solution != str(solution))
            or solution == "ERR"
        ):
            color = Console.Color.BOLD_RED
            symbol = "✘"
            run_result = False

        print(Console.with_color(f"{symbol} {year} | {day} | part{part:02d} => {solution}", color))
    return run_result


for part in [1, 2]:
    print(Console.with_color("\n##################################", Console.Color.BOLD_CYAN))
    print(Console.with_color(f"#             PART {part}             #", Console.Color.BOLD_CYAN))
    print(Console.with_color("##################################\n", Console.Color.BOLD_CYAN))

    # 2021 does not support testdata
    if "2021" in year:
        run_with_file("data", part)
    else:
        if run_with_file("testdata", part):
            run_with_file("data", part)
        else:
            break
        
