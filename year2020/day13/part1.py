def run(data: list[str], is_test: bool):
    earliest = int(data[0])
    buses = [int(bus) for bus in data[1].split(",") if bus != "x"]
    times = sorted([(bus - earliest % bus, bus) for bus in buses], key=lambda x: x[0])
    return times[0][0] * times[0][1]
