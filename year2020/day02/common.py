import re


def parse_input_data(data: list[str]):
    return [
        (count.split("-"), letter, password) for count, letter, password in [re.split(":?[ ]", line) for line in data]
    ]
