def get_data():
    with open('day14/data') as f:
        sequence = [c for c in f.readline().strip()]
        rules = {
            pair: insert
            for pair, insert in [
                line.strip().split(' -> ') for line in f.readlines()
                if len(line.strip()) > 0
            ]
        }
        return [sequence, rules]
