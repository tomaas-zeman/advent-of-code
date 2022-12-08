from year2019.day1.common import fuel_amount


def fuel_recursive(fuel: int, mass: int):
    fuel_for_mass = fuel_amount(mass)

    if fuel_for_mass <= 0:
        return fuel

    return fuel_recursive(fuel + fuel_for_mass, fuel_for_mass)


def run(data: list[str], raw_data: list[str]):
    return sum([fuel_recursive(0, int(mass)) for mass in data])
