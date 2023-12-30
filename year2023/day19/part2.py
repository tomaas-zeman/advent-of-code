from functools import reduce
from operator import lt, mul

from portion import Interval, CLOSED, OPEN, closedopen, openclosed, closed

from year2023.day19.common import Workflow, parse


def interval_length(interval: Interval) -> int:
    def correction(part: Interval) -> int:
        if part.left == CLOSED == part.right:
            return 1
        if part.left == OPEN == part.right:
            return -1
        return 0

    return sum(p.upper - p.lower + correction(p) for p in interval)


def combinations(intervals: dict[str, Interval]):
    return reduce(mul, [interval_length(intervals[k]) for k in "xmas"], 1)


def solve(
    workflows: dict[str, Workflow], workflow: Workflow, intervals: dict[str, Interval]
) -> int:
    result = 0

    for rule in workflow.rules:
        success_rule_interval = (
            closedopen(1, rule.value) if rule.op == lt else openclosed(rule.value, 4000)
        )
        failure_rule_interval = closed(1, 4000) - success_rule_interval

        # success path
        success_intervals = dict(intervals)
        success_intervals[rule.prop] &= success_rule_interval
        if rule.dest == "A":
            result += combinations(success_intervals)
        elif rule.dest != "R":
            result += solve(workflows, workflows[rule.dest], success_intervals)

        # fail path - continue with the next rule
        intervals[rule.prop] &= failure_rule_interval

    if workflow.final_destination == "A":
        result += combinations(intervals)
    elif workflow.final_destination != "R":
        result += solve(workflows, workflows[workflow.final_destination], intervals)

    return result


def run(data: list[str], is_test: bool):
    workflows, _ = parse(data)
    initial_interval = {p: closed(1, 4000) for p in "xmas"}
    return solve(workflows, workflows["in"], dict(initial_interval))
