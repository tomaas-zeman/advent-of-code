import re
from typing import List, Tuple


def parse_input_data(data: List[str]) -> List[Tuple[Tuple[int, int], str, str]]:
    return [
        (count.split('-'), letter, password)
        for count, letter, password in
        [re.split(':?[ ]', line) for line in data]
    ]
