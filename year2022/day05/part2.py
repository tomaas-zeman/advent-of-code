from aocutils import raw_input
from year2022.day05.common import compute_result


@raw_input
def run(data: list[str], is_test: bool):
    return compute_result(data, bulk_move=True)
