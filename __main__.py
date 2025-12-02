import multiprocessing
import re
import traceback
from importlib import import_module
from os.path import exists
from sys import argv

import requests

from aocutils import measure_time, Console

#
# Expected format of input params
# [0] : working directory
# [1] : year/day
# [2] : part to run (optional)
#
# Run as: python -- . 2022/01
#         python -- . 2022/01 2
#
[year, day] = argv[1].split("/")
parts = [int(argv[2])] if len(argv) > 2 else [1, 2]


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
    module_obj = import_module(module)
    runnable = module_obj.run
    data = (
        data
        if getattr(runnable, "uses_raw_input", False)
        else [line.strip() for line in data]
    )

    if is_test:
        expected_test_solution = None
        if hasattr(module_obj, "test_result"):
            expected_test_solution = str(getattr(module_obj, "test_result"))
        solution = runnable(data, is_test=is_test)
        return solution, expected_test_solution

    return runnable(data, is_test=is_test), None


def run_with_file(filename: str, part: int):
    run_result = True
    is_test = filename.startswith("testdata")
    input_file = f"year{year}/day{day}/{filename}"

    # skip tests if we don't have test data
    if is_test and not exists(input_file):
        return True

    # support different testdata for each part
    if part == 2 and filename == "testdata" and exists(f"{input_file}2"):
        input_file = f"{input_file}2"

    download_input_file()
    expected_test_solution = None
    with open(input_file, "r") as file:
        try:
            module = f"year{year}.day{day}.part{part}"
            solution, expected_test_solution = compute_solution(
                module, part, file.readlines(), is_test=is_test
            )
        except Exception:
            solution = "ERR"
            print(traceback.format_exc())
            run_result = False

        color = None
        symbol = "✔"
        if (
            solution is None
            or (
                expected_test_solution is not None
                and expected_test_solution != str(solution)
            )
            or solution == "ERR"
        ):
            color = Console.Color.BOLD_RED
            symbol = "✘"
            run_result = False

        print(
            Console.with_color(
                f"{symbol} year {year} | day {day} | part{part:02d} => {solution}",
                color,
            )
        )
        if not is_test:
            send_answer(str(part), str(solution))
    return run_result


def save_correct_answer(part: str, answer: str):
    with open("answers.txt", "a") as answers_file:
        answers_file.write(f"{year}-{day}-{part}={answer}\n")


def get_correct_answer(part: str):
    with open("answers.txt", "r") as answers_file:
        for line in answers_file.readlines():
            if line.startswith(f"{year}-{day}-{part}="):
                return line.split("=")[1].strip()
    return None


def send_answer(part: str, answer: str):
    if get_correct_answer(part) is not None:
        if get_correct_answer(part) == answer:
            Console.yellow("> You already submitted a correct answer for this part.")
        else:
            Console.red(
                "> You already submitted a correct answer for this part but it's incorrect NOW"
            )
        return

    choice = input(f"> Send answer '{answer}' to AOC for verification? [y/N] ")
    if choice.lower() != "y":
        return

    with open(".session", "r") as session_file:
        session = session_file.readline().strip()
        response = requests.post(
            url=f"https://adventofcode.com/{year}/day/{int(day)}/answer",
            cookies={"session": session},
            data={"level": part, "answer": answer},
        )

        if response.ok:
            if "You gave an answer too recently" in response.text:
                Console.red(
                    "> You submitted an answer too recently. Try again in a few minutes."
                )
            elif "not the right answer" in response.text:
                if "too low" in response.text:
                    Console.red("> Incorrect answer - too low.")
                elif "too high" in response.text:
                    Console.red("> Incorrect answer - too high.")
                else:
                    Console.red("> Incorrect answer")
                wait_before_retry = re.search(
                    r"([Pp]lease wait .* trying again\.)", response.text
                ).group(1)
                Console.yellow(f"> {wait_before_retry}")
            elif "seem to be solving the right level." in response.text:
                Console.yellow("> Wrong level or already solved.")
            else:
                Console.green("> CORRECT!")
                save_correct_answer(part, answer)
        else:
            Console.red(f"> {response.text}")


if __name__ == "__main__":
    multiprocessing.freeze_support()

    for part in parts:
        Console.bold_cyan("\n##################################")
        Console.bold_cyan(f"#             PART {part}             #")
        Console.bold_cyan("##################################\n")

        if run_with_file("testdata", part):
            run_with_file("data", part)
        else:
            break
