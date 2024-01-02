from collections import defaultdict

from aocutils import as_ints


def find_nth_number(data: list[str], limit: int):
    initial_sequence = as_ints(data[0].split(","))
    numbers_in_turns = defaultdict(list, {n: [i + 1] for i, n in enumerate(initial_sequence)})

    turn = len(initial_sequence) + 1
    last_number = initial_sequence[-1]

    while turn <= limit:
        if len(numbers_in_turns[last_number]) == 1:
            last_number = 0
            numbers_in_turns[last_number].append(turn)
        else:
            last_number = numbers_in_turns[last_number][-1] - numbers_in_turns[last_number][-2]
            numbers_in_turns[last_number].append(turn)

        turn += 1

    return last_number
