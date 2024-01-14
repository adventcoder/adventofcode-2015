from utils import get_input, tabulate
from itertools import combinations
from math import inf

weapons = [(8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74, 8, 0)]
armors = [(13, 0, 1), (31, 0, 2), (53, 0, 3), (75, 0, 4), (102, 0, 5)]
rings = [(25, 1, 0), (50, 2, 0), (100, 3, 0), (20, 0, 1), (40, 0, 2), (80, 0, 3)]

def parse_boss(s):
    vals = { lval: int(rval) for lval, rval in tabulate(s, ':', maxsplit=1) }
    return vals['Hit Points'], vals['Damage'], vals['Armor']

boss_hp, boss_damage, boss_armor = parse_boss(get_input(21))
player_hp = 100

def player_lifetime(armor):
    return -((-player_hp) // max(boss_damage - armor, 1))

def boss_lifetime(damage):
    return -((-boss_hp) // max(damage - boss_armor, 1))

least_cost = inf
most_cost = 0
for weapon in weapons:
    for num_armors in (0, 1):
        for armor_comb in combinations(armors, num_armors):
            for num_rings in (0, 1, 2):
                for ring_comb in combinations(rings, num_rings):
                    items = (weapon, ) + armor_comb + ring_comb
                    total_cost, total_damage, total_armor = map(sum, zip(*items))
                    if player_lifetime(total_armor) >= boss_lifetime(total_damage):
                        least_cost = min(least_cost, total_cost)
                    else:
                        most_cost = max(most_cost, total_cost)
print('1.', least_cost)
print('2.', most_cost)
