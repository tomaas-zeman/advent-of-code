from year2022.day03.common import letter_value


def run(data: list[str], is_test: bool):
    sum = 0
    for line in data:
        first = line[0 : len(line) // 2]
        second = line[len(line) // 2 :]
        common_letter = set(first).intersection(second).pop()
        sum += letter_value(ord(common_letter))
    return sum


test_result = 157
