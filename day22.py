from utils import get_input
from dataclasses import dataclass, replace
from math import inf

#TODO: could be cleaned up a bit

def parse_vals(s, labels):
    vals = [None] * len(labels)
    for line in s.splitlines():
        lval, rval = line.split(':')
        vals[labels.index(lval.strip())] = int(rval)
    return vals

boss_hp, boss_damage = parse_vals(get_input(22), ['Hit Points', 'Damage'])

def battle(hard):
    states = { State.start(hard): 0 }
    while states:
        state = min(states, key=states.get)
        mana_spent = states.pop(state)
        if state.player_hp <= 0:
            continue
        if state.boss_hp <= 0:
            return mana_spent
        for new_mana_spent, new_state in state.step(mana_spent, hard):
            if new_mana_spent < states.get(new_state, inf):
                states[new_state] = new_mana_spent

@dataclass(unsafe_hash=True)
class State:
    boss_hp: int = boss_hp
    player_hp: int = 50
    mana_gained: int = 500
    shield_timer: int = 0
    poison_timer: int = 0
    recharge_timer: int = 0

    @classmethod
    def start(cls, hard):
        state = cls()
        if hard:
            state.player_hp -= 1
        state.apply_effects()
        return state

    def step(self, mana_spent, hard):
        for new_mana_spent, new_state in self.player_attack(mana_spent):
            new_state.apply_effects()
            if new_state.boss_hp > 0:
                new_state.boss_attack()
                if hard:
                    new_state.player_hp -= 1
                new_state.apply_effects()
            yield new_mana_spent, new_state

    def player_attack(self, mana_spent):
        mana = self.mana_gained - mana_spent
        if mana >= 53:
            yield mana_spent + 53, replace(self, boss_hp=self.boss_hp-4)
        if mana >= 73:
            yield mana_spent + 73, replace(self, boss_hp=self.boss_hp-2, player_hp=self.player_hp+2)
        if mana >= 113 and self.shield_timer == 0:
            yield mana_spent + 113, replace(self, shield_timer=6)
        if mana >= 173 and self.poison_timer == 0:
            yield mana_spent + 173, replace(self, poison_timer=6)
        if mana >= 229 and self.recharge_timer == 0:
            yield mana_spent + 229, replace(self, recharge_timer=5)

    def boss_attack(self):
        player_armor = 7 if self.shield_timer > 0 else 0
        self.player_hp -= max(boss_damage - player_armor, 1)

    def apply_effects(self):
        if self.shield_timer > 0:
            self.shield_timer -= 1
        if self.poison_timer > 0:
            self.boss_hp -= 3
            self.poison_timer -= 1
        if self.recharge_timer > 0:
            self.recharge_timer -= 1
            self.mana_gained += 101

print('1.', battle(False))
print('2.', battle(True))
