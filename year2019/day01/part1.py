from year2019.day01.common import fuel_amount


def run(data: list[str], raw_data: list[str]):
    return sum([fuel_amount(int(mass)) for mass in data])
