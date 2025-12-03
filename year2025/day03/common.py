from aocutils import as_ints


def calculate_joltage_rating(data: list[str], digits: int):
    rating = 0

    for numbers in [as_ints(line) for line in data]:
        sequence = ""

        while len(sequence) < digits:
            candidates = numbers[: len(numbers) - (digits - 1 - len(sequence))]
            max_digit = max(candidates)
            sequence += str(max_digit)
            numbers = numbers[numbers.index(max_digit) + 1 :]

        rating += int(sequence)

    return rating
