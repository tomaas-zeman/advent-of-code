def get_data():
    with open('day1/data') as f:
        return [int(x) for x in f.readlines() if len(x) > 0]
