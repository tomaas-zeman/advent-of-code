from operator import gt, lt
import re


class Part:
    def __init__(self, props: dict[str, int]):
        self.props = props


class Rule:
    def __init__(self, prop: str, op: str, value: str, dest: str):
        self.prop = prop
        self.op = {"<": lt, ">": gt}[op]
        self.value = int(value)
        self.dest = dest

    def accepts(self, value: int):
        return self.op(value, self.value)


class Workflow:
    def __init__(self, rules: list[Rule], final_destination: str):
        self.rules = rules
        self.final_destination = final_destination

    def next(self, part: Part) -> str:
        for rule in self.rules:
            if rule.accepts(part.props[rule.prop]):
                return rule.dest
        return self.final_destination


def parse(data: list[str]) -> tuple[dict[str, Workflow], list[Part]]:
    raw_workflows = data[: data.index("")]
    raw_parts = data[data.index("") + 1 :]

    workflows = {}
    for rw in raw_workflows:
        name = rw.split("{")[0]
        rules = [Rule(*m) for m in re.findall("(\w+)([<>])(\d+):(\w+)", rw)]
        final_destination = rw.split(",")[-1][:-1]
        workflows[name] = Workflow(rules, final_destination)

    parts = [
        Part({m[0]: int(m[1]) for m in re.findall("(\w)=(\d+)", rp)})
        for rp in raw_parts
    ]
    return workflows, parts
