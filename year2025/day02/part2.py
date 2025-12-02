from aocutils import as_ints


def run(data: list[str], is_test: bool):
    invalid_ids = []

    for bounds in data[0].split(","):
        [min, max] = as_ints(bounds.split("-"))
        for number in range(min, max + 1):
            if is_invaid(number):
                invalid_ids.append(number)

    return sum(invalid_ids)


def is_invaid(number):
    seq = str(number)
    for length in range(1, len(seq) // 2 + 1):
        if len(seq) % length != 0:
            continue
        pattern = seq[0:length]
        repeats = len(seq) // len(pattern)
        if seq == pattern * repeats:
            return True

    return False


test_result = 4174379265
