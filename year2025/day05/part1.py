from year2025.day05.common import parse_input


def run(data: list[str], is_test: bool):
    [interval, ingredients] = parse_input(data)
    return len([i for i in ingredients if interval.contains(i)])
    
    
test_result = 3