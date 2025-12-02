from aocutils import as_ints


def run(data: list[str], is_test: bool):
    sum = 0

    for bounds in data[0].split(","):
        [min, max] = as_ints(bounds.split("-"))
        for number in range(min, max + 1):
            seq = str(number)
            first_half = seq[: len(seq) // 2]
            second_half = seq[len(seq) // 2 :]
            if first_half == second_half:
                sum += number

    return sum


test_result = 1227775554
