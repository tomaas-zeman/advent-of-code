import re

from aocutils import as_ints


def run(data: list[str], is_test: bool):
    return sum(as_ints(re.findall("(-?\d+)", data[0])))
