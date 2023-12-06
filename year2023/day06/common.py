def compute(races: list[tuple[int, int]]):
    result = 1
    for time, record in races:
        options = 0
        for speed in range(time):
            if speed * (time - speed) > record:
                options += 1
        result *= options
    return result
