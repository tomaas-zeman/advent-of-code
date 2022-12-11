def get_data():
    with open("year2021/day02/data") as f:
        return [(x.split(" ")[0], int(x.split(" ")[1])) for x in f.readlines() if len(x) > 0]
