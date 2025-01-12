from random import shuffle


def run(data: list[str], is_test: bool):
    rules = [line.split(" => ") for line in data[:-2]]

    molecule = data[-1]
    steps = 0

    while len(molecule) > 1:
        prev = molecule

        for src, dst in rules:
            while dst in molecule:
                steps += molecule.count(dst)
                molecule = molecule.replace(dst, src)

        if prev == molecule:
            shuffle(rules)
            molecule = data[-1]
            steps = 0

    return steps
