def replace(molecule: str, src: str, replacement: str, index: int):
    return f"{molecule[0:index]}{replacement}{molecule[index+len(src):]}"


def run(data: list[str], is_test: bool):
    rules = [line.split(" => ") for line in data[:-2]]
    molecule = data[-1]

    calibration = set()

    for i in range(len(molecule)):
        for src, dst in rules:
            if molecule[i : i + len(src)] == src:
                calibration.add(replace(molecule, src, dst, i))

    return len(calibration)


test_result = 4
