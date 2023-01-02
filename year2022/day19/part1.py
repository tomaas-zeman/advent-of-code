from __future__ import annotations
from year2022.day19.common import Resources, Robot, Type, parse_input
from queue import PriorityQueue


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

    def __hash__(self):
        return hash(self.id)

    def __str__(self):
        return f"{self.resources} | {' '.join(r.type.name for r in self.robots)}"


def try_to_build_a_robot(state: State, robot: Robot, resource_limits: dict[Type, int]):
    if state.resources.enough_for(robot) and (
        resource_limits[robot.type] == 0 or state.resources[robot.type] < resource_limits[robot.type]
    ):
        new_resources = state.resources.add_mined_with(state.robots).pay_for(robot)
        new_state = State(new_resources, state.robots + [robot], state.time_left - 1)
        return (-robot.type.value, new_state)


def run(data: list[str], is_test: bool):
    blueprints = parse_input(data)

    results: dict[int, int] = {}

    for bp in blueprints:
        resource_limits = {type: max([robot.cost[type.value] for robot in bp.robots()]) for type in Type.all()}

        states = PriorityQueue[tuple[int, State]]()
        states.put((0, State(robots=[Robot(Type.ORE)])))
        cache: dict[State, int] = {}

        while not states.empty():
            priority, state = states.get()

            if cache.get(state, 0) > state.resources[Type.GEODE]:
                continue
            else:
                cache[state] = state.resources[Type.GEODE]

            if state.time_left == 0:
                results[bp.id] = state.resources[Type.GEODE]
                continue

            next_states = [
                new_state
                for new_state in [try_to_build_a_robot(state, robot, resource_limits) for robot in bp.robots()]
                if new_state is not None
            ]

            if len(next_states) > 0:
                states.put(next_states[-1])  # the last one has robots with the highest priority
            else:
                states.put(
                    (priority, State(state.resources.add_mined_with(state.robots), state.robots, state.time_left - 1))
                )

    return sum([id * res for id, res in results.items()])
