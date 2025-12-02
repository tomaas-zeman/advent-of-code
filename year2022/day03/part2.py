from year2022.day03.common import letter_value


def run(data: list[str], is_test: bool):
    sum = 0
    groups = [data[i : i + 3] for i in range(0, len(data), 3)]
    for group in groups:
        common_letter = set(group[0]).intersection(group[1]).intersection(group[2]).pop()
        sum += letter_value(ord(common_letter))
    return sum


test_result = 70
