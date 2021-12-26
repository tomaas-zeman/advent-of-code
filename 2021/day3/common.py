def get_data():
    with open('day3/data') as f:
        return [[int(bit) for bit in line.strip()] for line in f.readlines() if len(line) > 0]
