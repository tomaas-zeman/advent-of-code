def run(data: list[str], is_test: bool):
    time = int("".join(data[0].split(":")[1].split()))
    record = int("".join(data[1].split(":")[1].split()))
    options = 0
    for speed in range(time):
        if speed * (time - speed) > record:
            options += 1
    return options
