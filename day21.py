from utils import get_input
from itertools import combinations
from math import inf

weapons = [(8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74, 8, 0)]
armors = [(13, 0, 1), (31, 0, 2), (53, 0, 3), (75, 0, 4), (102, 0, 5)]
rings = [(25, 1, 0), (50, 2, 0), (100, 3, 0), (20, 0, 1), (40, 0, 2), (80, 0, 3)]

def parse_vals(s, labels):
    vals = [None] * len(labels)
    for line in s.splitlines():
        lval, rval = line.split(':')
        vals[labels.index(lval.strip())] = int(rval)
    return vals

boss_hp, boss_damage, boss_armor = parse_vals(get_input(21), ['Hit Points', 'Damage', 'Armor'])
player_hp = 100

def player_turns(player_armor):
    return -((-player_hp) // max(boss_damage - player_armor, 1))

def boss_turns(player_damage):
    return -((-boss_hp) // max(player_damage - boss_armor, 1))

least_cost = inf
most_cost = 0
for weapon in weapons:
    for num_armors in (0, 1):
        for armor_comb in combinations(armors, num_armors):
            for num_rings in (0, 1, 2):
                for ring_comb in combinations(rings, num_rings):
                    items = (weapon, ) + armor_comb + ring_comb
                    total_cost, total_damage, total_armor = map(sum, zip(*items))
                    if player_turns(total_armor) >= boss_turns(total_damage):
                        least_cost = min(least_cost, total_cost)
                    else:
                        most_cost = max(most_cost, total_cost)
print('1.', least_cost)
print('2.', most_cost)
