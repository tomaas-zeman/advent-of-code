def decode_line_patterns(patterns, output):
    decoded_numbers = {}
    patterns_by_length = {}

    for pattern in patterns:
        length = len(pattern)
        if length not in patterns_by_length:
            patterns_by_length[length] = []
        patterns_by_length[length].append(''.join(sorted(pattern)))

    for length in range(2, 8):
        if length == 2:
            decoded_numbers[1] = patterns_by_length[2][0]
        elif length == 3:
            decoded_numbers[7] = patterns_by_length[3][0]
        elif length == 4:
            decoded_numbers[4] = patterns_by_length[4][0]
        elif length == 5:
            for pattern in patterns_by_length[5]:
                if all([c in pattern for c in decoded_numbers[1]]):
                    decoded_numbers[3] = pattern
                elif all([c in pattern for c in decoded_numbers[4] if c not in decoded_numbers[1]]):
                    decoded_numbers[5] = pattern
                else:
                    decoded_numbers[2] = pattern
        elif length == 6:
            for pattern in patterns_by_length[6]:
                if all([c in pattern for c in decoded_numbers[1]]):
                    if set(decoded_numbers[2]) \
                            .intersection(set(decoded_numbers[4])) \
                            .intersection(set(decoded_numbers[5])) \
                            .pop() in pattern:
                        decoded_numbers[9] = pattern
                    else:
                        decoded_numbers[0] = pattern
                else:
                    decoded_numbers[6] = pattern
        elif length == 7:
            decoded_numbers[8] = patterns_by_length[7][0]

    reversed_decoded_numbers = {segments: number for number, segments in decoded_numbers.items()}

    decoded_output = []
    for number_in_output in output:
        decoded_output.append(reversed_decoded_numbers[''.join(sorted(number_in_output))])

    return decoded_output


def get_data():
    with open('day8/data') as f:
        data = []

        lines = [x.strip() for x in f.readlines()]
        for line in lines:
            [patterns, output] = line.split('|')
            data.append((patterns.strip().split(' '), output.strip().split(' ')))

        return data
