def parse(data: list[str]):
    return [(x.split(" ")[0], int(x.split(" ")[1])) for x in data]
