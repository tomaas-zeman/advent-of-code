def get_data():
    with open('day10/data') as f:
        return [x.strip() for x in f.readlines()]
