from itertools import pairwise


def is_nice(string: str) -> bool:
    pairs_found = False

    for i in range(len(string) - 1):
        pair = (string[i], string[i + 1])
        for subpair in pairwise(string[i + 2 :]):
            if pair == subpair:
                pairs_found = True

    if not pairs_found:
        return False

    for i in range(len(string) - 2):
        if string[i] == string[i + 2]:
            return True

    return False


def run(data: list[str], is_test: bool):
    return len([s for s in data if is_nice(s)])
