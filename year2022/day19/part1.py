from __future__ import annotations

from year2022.day19.common import Blueprint, Resources, Robot, Type, parse_input


class State:
    def __init__(
        self,
        resources: Resources = Resources(),
        robots: list[Robot] = [],
        time_left: int = 24,
    ):
        self.resources = resources
        self.robots = robots
        self.time_left = time_left
        self.id = (
            self.resources,
            self.time_left,
            tuple([r.type for r in sorted(self.robots, key=lambda r: r.type.value)]),
        )

    def robots_by_type(self, type: Type):
        return [robot for robot in self.robots if robot.type == type]

    def next(self):
        return State(self.resources.add_mined_with(self.robots), self.robots, self.time_left - 1)

    def __hash__(self):
        return hash(self.id)

    def __str__(self):
        return f"{self.resources} | {' '.join(r.type.name for r in self.robots)}"


def generate_next_states(bp: Blueprint, state: State, resource_limits: dict[Type, int]):
    def not_over_limit(robot: Robot):
        return resource_limits[robot.type] == 0 or state.resources[robot.type] < resource_limits[robot.type]

    def next_state_with_new_robot(robot: Robot):
        return State(
            state.resources.add_mined_with(state.robots).pay_for(robot), state.robots + [robot], state.time_left - 1
        )

    # order: regular robots, wait, geode robot
    next_states = []
    for robot in bp.robots()[:3] + [None] + bp.robots()[3:]:
        if robot is None:
            next_states.append(state.next())
        elif state.resources.enough_for(robot) and not_over_limit(robot):
            next_states.append(next_state_with_new_robot(robot))

    return next_states


def run(data: list[str], is_test: bool):
    blueprints = parse_input(data)

    results: dict[int, int] = {}

    for bp in blueprints[:1]:
        resource_limits = {type: max([robot.cost[type.value] for robot in bp.robots()]) for type in Type.all()}

        states = [State(robots=[Robot(type=Type.ORE)])]
        # cache: dict[State, int] = {}

        while len(states) > 0:
            state = states.pop()

            # if cache.get(state, 0) > state.resources[Type.GEODE]:
            #     continue
            # else:
            #     cache[state] = state.resources[Type.GEODE]

            if state.time_left <= 0:
                results[bp.id] = max(state.resources[Type.GEODE], results.get(bp.id, 0))
                continue

            if (
                state.robots_by_type(Type.GEODE) == 0
                and state.time_left < bp.geode_robot.cost[Type.OBSIDIAN] - state.resources[Type.OBSIDIAN]
            ):
                continue

            next_states = generate_next_states(bp, state, resource_limits)

            if len(next_states) > 0:
                for next_state in next_states:
                    states.append(next_state)
            else:
                states.append(State(state.resources.add_mined_with(state.robots), state.robots, state.time_left - 1))

    return sum([id * res for id, res in results.items()])
