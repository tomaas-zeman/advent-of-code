from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
import re
from typing import Tuple
from aocutils import as_ints


class Spell(Enum):
    MAGIC_MISSILE = 53
    DRAIN = 73
    SHIELD = 113
    POISON = 173
    RECHARGE = 229

    @classmethod
    def all(cls):
        return [cls.DRAIN, cls.MAGIC_MISSILE, cls.POISON, cls.RECHARGE, cls.SHIELD]


@dataclass(init=True)
class Player:
    hp: int
    dmg: int
    armor: int
    mana: int
    effects: list[Tuple[Spell, int]]

    def effect_names(self):
        return [e for e, _ in self.effects]

    def clone(self):
        return Player(
            self.hp, self.dmg, self.armor, self.mana, [(e, t) for e, t in self.effects]
        )

    def cast(self, defender: Player, spell: Spell):
        self.mana -= spell.value

        if spell == Spell.MAGIC_MISSILE:
            defender.hp -= 4
        elif spell == Spell.DRAIN:
            defender.hp -= 2
            self.hp += 2
        elif spell == Spell.SHIELD:
            self.effects.append((Spell.SHIELD, 6))
        elif spell == Spell.POISON:
            defender.effects.append((Spell.POISON, 6))
        elif spell == Spell.RECHARGE:
            self.effects.append((Spell.RECHARGE, 5))

    def resolve_effects(self):
        next_effects = []

        for effect, remaining_time in self.effects:
            if effect == Spell.POISON:
                self.hp -= 3
            elif effect == Spell.RECHARGE:
                self.mana += 101
            elif effect == Spell.SHIELD:
                self.armor = 7

            if remaining_time > 1:
                next_effects.append((effect, remaining_time - 1))
            elif effect == Spell.SHIELD:
                self.armor = 0

        self.effects = next_effects

    def hit(self, defender: Player):
        defender.hp -= max(1, self.dmg - defender.armor)


def fight(data: list[str], hard_mode: bool, is_test: bool):
    me = Player(10, 0, 0, 250, []) if is_test else Player(50, 0, 0, 500, [])
    boss = Player(*as_ints(re.findall("\\d+", "".join(data))), 0, 0, [])

    min_mana_spent = float("inf")
    state: list[Tuple[Player, Player, int]] = [(me, boss, 0, True)]

    while len(state) > 0:
        me, boss, mana_spent, my_turn = state.pop()

        if hard_mode:
            me.hp -= 1

        me.resolve_effects()
        boss.resolve_effects()

        if boss.hp <= 0:
            if mana_spent < min_mana_spent:
                min_mana_spent = mana_spent
            continue

        if (
            me.hp <= 0
            or me.mana <= 0
            or mana_spent > min_mana_spent
            or all([spell.value > me.mana for spell in Spell.all()])
        ):
            continue

        if my_turn:
            for spell in Spell.all():
                if spell.value > me.mana:
                    continue
                if (
                    spell in [Spell.RECHARGE, Spell.SHIELD]
                    and spell in me.effect_names()
                ):
                    continue
                if spell == Spell.POISON and spell in boss.effect_names():
                    continue

                next_me = me.clone()
                next_boss = boss.clone()
                next_me.cast(next_boss, spell)

                state.append(
                    (next_me, next_boss, mana_spent + spell.value, not my_turn)
                )
        else:
            boss.hit(me)
            state.append((me, boss, mana_spent, not my_turn))

    return min_mana_spent
