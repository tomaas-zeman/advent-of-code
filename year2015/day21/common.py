from dataclasses import dataclass
from itertools import combinations
import re
from typing import Callable

from aocutils import Tuple, as_ints


weapons = [
    (8, 4, 0),
    (10, 5, 0),
    (25, 6, 0),
    (40, 7, 0),
    (74, 8, 0),
]
armor = [
    (0, 0, 0),
    (13, 0, 1),
    (31, 0, 2),
    (53, 0, 3),
    (75, 0, 4),
    (102, 0, 5),
]
rings = [
    (25, 1, 0),
    (50, 2, 0),
    (100, 3, 0),
    (20, 0, 1),
    (40, 0, 2),
    (80, 0, 3),
]


@dataclass
class Player:
    hp: int
    dmg: int
    armor: int


def hit(attacker: Player, defender: Player):
    defender.hp -= max(1, attacker.dmg - defender.armor)


def ring_combinations():
    rings = [
        [(0, 0, 0)],
    ]
    for n in range(1, 3):
        for c in combinations(rings, n):
            rings.append(c)
    return rings


def calculate_cost(
    data: list[str],
    player_dead_condition: Callable[[Player, Player], bool],
    cost_comparator: Callable[[int, int], int],
    initial_cost: int,
):
    cost = initial_cost

    for weapon in weapons:
        for rings in ring_combinations():
            for armor in armor:
                current_cost = weapon[0] + armor[0] + sum(r[0] for r in rings)

                me = Player(
                    100,
                    *Tuple.add((0, 0), weapon[1:], armor[1:], *[r[1:] for r in rings])
                )
                boss = Player(*as_ints(re.findall("\\d+", "".join(data))))

                my_turn = True
                while me.hp > 0 and boss.hp > 0:
                    if my_turn:
                        hit(me, boss)
                    else:
                        hit(boss, me)
                    my_turn = not my_turn

                if player_dead_condition(me, boss):
                    cost = cost_comparator(cost, current_cost)

    return cost
