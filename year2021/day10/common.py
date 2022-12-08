def get_data():
    with open("year2021/day10/data") as f:
        return [x.strip() for x in f.readlines()]
