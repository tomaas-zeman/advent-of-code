from year2021.day17.common import send_probes


def run(data: list[str], is_test: bool):
    return len(send_probes(data, is_test)[1])
