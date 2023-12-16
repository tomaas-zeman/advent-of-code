def run(data: list[str], is_test: bool):
    buses = [(int(bus), i) for i, bus in enumerate(data[1].split(",")) if bus != "x"]

    step = 1
    timestamp = 0
    for bus, offset in buses:
        while True:
            timestamp += step
            if (timestamp + offset) % bus == 0:
                step *= bus
                break

    return timestamp
