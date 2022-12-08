import re


class Passport:
    def __init__(self, fields: dict[str, str]):
        self.fields = fields

    def has_mandatory_fields(self):
        mandatory_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
        return all(field in self.fields for field in mandatory_fields)

    def is_valid(self):
        if not self.has_mandatory_fields():
            return False

        validation_rules = {
            "byr": lambda year: len(year) == 4 and 1920 <= int(year) <= 2002,
            "iyr": lambda year: len(year) == 4 and 2010 <= int(year) <= 2020,
            "eyr": lambda year: len(year) == 4 and 2020 <= int(year) <= 2030,
            "hgt": lambda height: re.match("^\\d+(cm|in)$", height)
            and (
                150 <= int(height.replace("cm", "")) <= 193
                if "cm" in height
                else 59 <= int(height.replace("in", "")) <= 76
            ),
            "hcl": lambda color: re.match("^#[0-9a-f]{6}$", color),
            "ecl": lambda color: color in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
            "pid": lambda pid: re.match("^\\d{9}$", pid),
            "cid": lambda _: True,
        }

        return all(validation_rules[field](value) for field, value in self.fields.items())


def parse_passports(data: list[str]):
    passports: list[Passport] = []

    current_fields = {}
    for line in data:
        if len(line) == 0:
            passports.append(Passport(current_fields))
            current_fields = {}
            continue
        current_fields.update({field.split(":")[0]: field.split(":")[1] for field in line.split(" ")})

    passports.append(Passport(current_fields))

    return passports
