import traceback
from importlib import import_module
from sys import argv
from common.utils import measure_time, Console
from os.path import exists
import requests
import re

#
# Expected format of input params
# [0] : <absolute file path>
# [1] : dir=<file dir relative to root>
#
# Run as: python main.py 2022/01
#
[year, day] = argv[1].split("/")


def download_input_file():
    input_file = f"year{year}/day{day}/data"
    if not exists(input_file):
        with open(".session", "r") as session_file:
            session = session_file.readline().strip()
            response = requests.get(
                url=f"https://adventofcode.com/{year}/day/{int(day)}/input",
                cookies={"session": session},
            )
            with open(input_file, "w") as input_file:
                input_file.write(re.sub("\n$", "", response.text))


@measure_time
def compute_solution(module: str, part: int, data: list[str], is_test: bool):
    # 2021 does not support autoparse
    if year == "2021":
        return (import_module(module).run(), None)

    runnable = import_module(module).run
    data = data if getattr(runnable, 'uses_raw_input', False) else [line.strip() for line in data]
    test_solution_prefix = "# part"

    if len(data) > 2 and data[0].startswith(test_solution_prefix) and data[1].startswith(test_solution_prefix):
        expected_test_solution = data[part - 1].split(" = ")[1].strip()
        solution = runnable(data[2:], is_test=is_test)
        return solution, expected_test_solution
    else:
        return runnable(data, is_test=is_test), None


def run_with_file(filename: str, part: int):
    run_result = True
    input_file = f"year{year}/day{day}/{filename}"
    download_input_file()
    expected_test_solution = None
    with open(input_file, "r") as file:
        try:
            module = f"year{year}.day{day}.part{part}"
            solution, expected_test_solution = compute_solution(
                module, part, file.readlines(), is_test=filename == "testdata"
            )
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

        print(Console.with_color(f"{symbol} year {year} | day {day} | part{part:02d} => {solution}", color))
    return run_result


for part in [1, 2]:
    print(Console.with_color("\n##################################", Console.Color.BOLD_CYAN))
    print(Console.with_color(f"#             PART {part}             #", Console.Color.BOLD_CYAN))
    print(Console.with_color("##################################\n", Console.Color.BOLD_CYAN))

    # 2021 does not support testdata
    if year == "2021":
        run_with_file("data", part)
    else:
        if run_with_file("testdata", part):
            run_with_file("data", part)
        else:
            break
