from collections import deque
from enum import Enum

PART2_END_MODULE = "qn"


class Pulse(Enum):
    LOW = 0
    HIGH = 1


class Signal:
    def __init__(self, source: str, destination: str, pulse: Pulse):
        self.source = source
        self.destination = destination
        self.pulse = pulse

    def __str__(self):
        return f"{self.source} -{self.pulse.name.lower()}-> {self.destination}"


class Module:
    def process(self, signal: Signal) -> list[Signal]:
        return []


class Generic(Module):
    def __init__(self, name: str):
        self.name = name
        self.destinations = []


class Button(Module):
    NAME = "button"

    def __init__(self):
        self.name = Button.NAME
        self.destinations = []

    def process(self, signal: Signal) -> list[Signal]:
        return [Signal(self.name, Broadcaster.NAME, Pulse.LOW)]


class Broadcaster(Module):
    NAME = "broadcaster"

    def __init__(self, destinations: list[str]):
        self.name = Broadcaster.NAME
        self.destinations = destinations

    def process(self, signal: Signal) -> list[Signal]:
        return [Signal(self.name, d, signal.pulse) for d in self.destinations]


class Conjunction(Module):
    PREFIX = "&"

    def __init__(self, name: str, destinations: list[str]):
        self.name = name
        self.destinations = destinations
        self.pulses = {}

    def add_input(self, input: str):
        self.pulses[input] = Pulse.LOW

    def process(self, signal: Signal) -> list[Signal]:
        if signal.source in self.pulses:
            self.pulses[signal.source] = signal.pulse
        pulse_to_send = Pulse.LOW if all(p == Pulse.HIGH for p in self.pulses.values()) else Pulse.HIGH
        return [Signal(self.name, d, pulse_to_send) for d in self.destinations]


class FlipFlop(Module):
    PREFIX = "%"

    def __init__(self, name: str, destinations: list[str]):
        self.name = name
        self.destinations = destinations
        self.is_on = False

    def process(self, signal: Signal) -> list[Signal]:
        if signal.pulse == Pulse.HIGH:
            return []
        self.is_on = not self.is_on
        pulse_to_send = Pulse.HIGH if self.is_on else Pulse.LOW
        return [Signal(self.name, d, pulse_to_send) for d in self.destinations]


def parse(data: list[str]) -> dict[str, Module]:
    modules = {Button.NAME: Button(), "output": Generic("output"), "rx": Generic("rx")}

    for line in data:
        name, destinations = line.split(" -> ")
        destinations = destinations.split(", ")

        if name == Broadcaster.NAME:
            modules[name] = Broadcaster(destinations)
        elif line.startswith(FlipFlop.PREFIX):
            name = name[1:]
            modules[name] = FlipFlop(name, destinations)
        elif line.startswith(Conjunction.PREFIX):
            name = name[1:]
            modules[name] = Conjunction(name, destinations)

    for name, module in modules.items():
        for dest in module.destinations:
            if isinstance(modules[dest], Conjunction):
                modules[dest].add_input(name)

    return modules


def push_button(modules) -> tuple[dict[Pulse, int], dict[str, Pulse]]:
    signal_count = {Pulse.LOW: 0, Pulse.HIGH: 0}
    end_module_sync_pulses = {}

    queue = deque(modules[Button.NAME].process([]))
    while len(queue) > 0:
        signal = queue.pop()
        signal_count[signal.pulse] += 1
        queue.extendleft(modules[signal.destination].process(signal))

        # Part 2 check
        if signal.destination == PART2_END_MODULE:
            for input, pulse in modules[signal.destination].pulses.items():
                if pulse == Pulse.HIGH:
                    end_module_sync_pulses[input] = pulse

    return signal_count, end_module_sync_pulses
