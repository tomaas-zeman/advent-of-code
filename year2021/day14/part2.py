from collections import Counter

from year2021.day14.common import get_data


def run():
    [seq, rules] = get_data()

    # empty
    chars = Counter(seq)
    pairs = {pair: 0 for pair in rules.keys()}

    # with initial sequence
    for i in range(len(seq) - 1):
        pairs[''.join(seq[i:i + 2])] += 1

    for step in range(40):
        active_pairs = [
            (pair, count)
            for pair, count in pairs.items() if count > 0
        ]

        for pair, count in active_pairs:
            pairs[pair] -= count
            pairs[f'{pair[0]}{rules[pair]}'] += count
            pairs[f'{rules[pair]}{pair[1]}'] += count
            chars[rules[pair]] += count

    return chars.most_common()[0][1] - chars.most_common()[-1][1]
