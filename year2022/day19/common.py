import re
from enum import Enum


class Type(Enum):
    ORE = 0
    CLAY = 1
    OBSIDIAN = 2
    GEODE = 3

    @staticmethod
    def all():
        return [Type.ORE, Type.CLAY, Type.OBSIDIAN, Type.GEODE]


class Robot:
    def __init__(self, type: Type, ore: int = 0, clay: int = 0, obsidian: int = 0):
        self.type = type
        self.cost = Resources((ore, clay, obsidian, 0))
        self.production = [1 if type == t else 0 for t in list(Type)]


def as_list(robots: list[Robot] | Robot) -> list[Robot]:
    return robots if isinstance(robots, list) else [robots]


class Resources:
    # resources: tuple[ore, clay, obsidian, geode]
    def __init__(self, resources: tuple[int, int, int, int] = (0, 0, 0, 0)):
        self.resources = resources

    def __getitem__(self, t: Type | int):
        if type(t) == int:
            return self.resources[t]
        return self.resources[t.value]

    def __hash__(self):
        return hash(self.resources)

    def enough_for(self, robots: list[Robot] | Robot):
        total_cost = [sum(r) for r in zip(*[r.cost.resources for r in as_list(robots)])]
        if not total_cost:
            return True
        return all([total_cost[i] <= self.resources[i] for i in range(len(total_cost))])

    def add_mined_with(self, robots: list[Robot] | Robot):
        return Resources(tuple([sum(res) for res in zip(self.resources, *[r.production for r in as_list(robots)])]))

    def pay_for(self, robots: list[Robot] | Robot):
        return Resources(
            tuple(
                [
                    sum(x)
                    for x in zip(
                        self.resources, *[map(lambda x: -x, robot.cost.resources) for robot in as_list(robots)]
                    )
                ]
            )
        )


class Blueprint:
    def __init__(self, id: int, ore_robot: Robot, clay_robot: Robot, obsidian_robot: Robot, geode_robot: Robot):
        self.id = id
        self.ore_robot = ore_robot
        self.clay_robot = clay_robot
        self.obsidian_robot = obsidian_robot
        self.geode_robot = geode_robot

    def robots(self):
        return [self.ore_robot, self.clay_robot, self.obsidian_robot, self.geode_robot]


def parse_input(data: list[str]):
    pattern = re.compile(
        r"Blueprint (\d+): .+ costs (\d+) ore. .+ costs (\d+) ore. .+ costs (\d+) ore and (\d+) clay. .+ costs (\d+) ore and (\d+) obsidian."
    )
    return [
        Blueprint(
            int(m[1]),
            Robot(Type.ORE, ore=int(m[2])),
            Robot(Type.CLAY, ore=int(m[3])),
            Robot(Type.OBSIDIAN, ore=int(m[4]), clay=int(m[5])),
            Robot(Type.GEODE, ore=int(m[6]), obsidian=int(m[7])),
        )
        for line in data
        if (m := pattern.match(line))
    ]
