from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from enum import Enum
from functools import reduce
from operator import ge, lt, eq, le, gt

from aocutils import Tuple, memoize


def as_list(robots: list[Robot] | Robot) -> list[Robot]:
    return robots if isinstance(robots, list) else [robots]


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
        self.production = Resources(tuple([1 if type == t else 0 for t in Type.all()]))


class Resources:
    # resources: tuple[ore, clay, obsidian, geode]
    def __init__(self, resources: tuple[int, ...] = (0, 0, 0, 0)):
        self.resources = resources

    def _compare(self, other: Resources, op):
        return all(op(self.resources[i], other.resources[i]) for i in range(len(self.resources)))

    def __eq__(self, other: Resources):
        return self._compare(other, eq)

    def __ge__(self, other: Resources):
        return self._compare(other, ge)

    def __gt__(self, other: Resources):
        return self._compare(other, gt)

    def __lt__(self, other: Resources):
        return self._compare(other, lt)

    def __le__(self, other: Resources):
        return self._compare(other, le)

    def __mul__(self, multiplier: int) -> Resources:
        if not isinstance(multiplier, int):
            raise Exception("Unsupported type for multiplication")
        return Resources(Tuple.mul(self.resources, multiplier))

    def __getitem__(self, t: Type | int) -> int:
        if isinstance(t, Type):
            return self.resources[t.value]
        return self.resources[t]

    def __add__(self, other: Resources) -> Resources:
        return Resources(Tuple.add(self.resources, other.resources))

    def __sub__(self, other: Resources) -> Resources:
        return Resources(Tuple.sub(self.resources, other.resources))


@dataclass(frozen=True)
class Blueprint:
    id: int
    ore_robot: Robot
    clay_robot: Robot
    obsidian_robot: Robot
    geode_robot: Robot

    def robots(self):
        return [self.ore_robot, self.clay_robot, self.obsidian_robot, self.geode_robot]

    @memoize
    def resource_limits(self):
        return Resources(
            tuple(
                [
                    max([r.cost[type] if type != Type.GEODE else sys.maxsize for r in self.robots()])
                    for type in Type.all()
                ]
            )
        )


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


@dataclass(frozen=True)
class State:
    resources: Resources
    robots: list[Robot]
    time_passed: int

    def next(self) -> State:
        return State(self.resources + self.produces(), self.robots, self.time_passed + 1)

    def produces(self, turns: int = 1) -> Resources:
        return reduce(lambda acc, prod: acc + prod, [r.production * turns for r in self.robots], Resources())

    def robots_of_type(self, type: Type):
        return len([r for r in self.robots if r.type == type])

    @staticmethod
    def hashable_robots(robots: list[Robot]):
        return tuple(sorted([r.type.value for r in robots]))

    def __hash__(self):
        return hash(self.time_passed) + hash(self.resources.resources) + hash(State.hashable_robots(self.robots))

    def __eq__(self, other: State):
        return (
            self.time_passed == other.time_passed
            and self.resources == other.resources
            and State.hashable_robots(self.robots) == State.hashable_robots(other.robots)
        )


def turns_to_activate_robot(robot: Robot, state: State):
    for turn in range(max(robot.cost.resources)):
        resources = state.produces(turn) + state.resources
        if resources >= robot.cost:
            return turn + 1
    return None


def waiting_results_in_the_same_robots(bp: Blueprint, state: State):
    robots_to_buy_now = [r for r in bp.robots() if state.resources >= r.cost]
    robots_to_buy_next_turn = [r for r in bp.robots() if state.resources + state.produces() >= r.cost]
    return len(robots_to_buy_now) > 0 and State.hashable_robots(robots_to_buy_now) == State.hashable_robots(
        robots_to_buy_next_turn
    )


def get_next_states(bp: Blueprint, state: State, max_time: int) -> list[State]:
    # Don't wait just to get the same robot as we can get now
    next_states = [] if waiting_results_in_the_same_robots(bp, state) else [state.next()]

    for robot in bp.robots():
        # Don't build more robots than we need
        if state.resources[robot.type] >= bp.resource_limits()[robot.type]:
            continue

        turns = turns_to_activate_robot(robot, state)
        if turns is not None and state.time_passed + turns <= max_time:
            next_states.append(
                State(
                    state.resources + state.produces(turns) - robot.cost,
                    state.robots + [robot],
                    state.time_passed + turns,
                )
            )

    return next_states


def get_geodes_opened(data: list[str], max_time: int) -> dict[int, int]:
    blueprints = parse_input(data)

    geodes_opened: dict[int, int] = {}

    for bp in blueprints:
        states = [State(Resources(), [Robot(type=Type.ORE)], 0)]
        visited = set()
        max_geodes = 0

        while len(states) > 0:
            state = states.pop()

            if state.time_passed == max_time:
                max_geodes = max(state.resources[Type.GEODE], max_geodes)
                continue

            if state in visited:
                continue
            visited.add(state)

            # Stop if we can't get more geodes even if we built GEODE robot each minute
            time_remaining = max_time - state.time_passed
            max_theoretical_geodes = (
                (time_remaining * (time_remaining + 1)) / 2
                + state.resources[Type.GEODE]
                + state.robots_of_type(Type.GEODE) * (max_time - state.time_passed)
            )
            if max_theoretical_geodes < max_geodes:
                continue

            states.extend(get_next_states(bp, state, max_time))

        geodes_opened[bp.id] = max_geodes

    return geodes_opened
