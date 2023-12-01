import re

def run(data: list[str], is_test: bool):
    sum = 0
    for line in data:
        numbers = re.findall("\\d", line)
        if len(numbers) > 0:
            sum += int(f"{numbers[0]}{numbers[-1]}")
    return sum
