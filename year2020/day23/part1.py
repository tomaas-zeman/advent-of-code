from year2020.day23.common import parse, make_steps


def run(data: list[str], is_test: bool):
    data = parse(data, [])
    make_steps(data, 10 if is_test else 100)

    result = []
    cup = data.cups_by_value[1]
    while cup.next.value != 1:
        cup = cup.next
        result.append(cup.value)

    return "".join([str(c) for c in result])


test_result = 92658374
