def generate_sequences(initial_sequence: list[int]):
    sequences = [initial_sequence]

    while True:
        new_sequence = [sequences[-1][i + 1] - sequences[-1][i] for i in range(len(sequences[-1]) - 1)]
        sequences.append(new_sequence)
        if all(n == 0 for n in new_sequence):
            break

    return sequences


def calculate_next_number(initial_sequence: list[int]):
    return sum([s[-1] for s in generate_sequences(initial_sequence)])