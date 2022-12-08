def get_data():
    with open("year2021/day6/data") as f:
        return [int(x) for x in f.readline().strip().split(",")]
