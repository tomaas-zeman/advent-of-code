from collections import Counter

from year2021.day14.common import get_data


def run():
    [seq, rules] = get_data()

    for step in range(10):
        index = 0
        while index < len(seq) - 1:
            key = ''.join(seq[index:index + 2])
            if key in rules:
                seq.insert(index + 1, rules[key])
                index += 1
            index += 1

    count = Counter(seq)
    return count.most_common()[0][1] - count.most_common()[-1][1]
