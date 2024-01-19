from utils import get_input
from collections import defaultdict, Counter
from functools import cache
from math import inf
import re

def parse_molecule(s):
    return re.findall(r'[A-Z][a-z]*', s)

def parse_rules(s):
    rules = defaultdict(list)
    for line in s.splitlines():
        lval, rval = line.split('=>', maxsplit=1)
        rules[lval.strip()].append(parse_molecule(rval))
    return rules

def reverse(rules):
    # Convert the rules to C.N.F. and reverse.
    #
    # Al => [Th, Rn, F, Ar]
    #
    # (Th, RnFAr) => Al
    # (Rn, FAr) => RnFAr
    # (F, Ar) => FAr
    #
    reductions = {}
    for atom in rules:
        for sub in rules[atom]:
            prev = atom
            for i in range(len(sub) - 1):
                suffix = ''.join(sub[i+1:])
                reductions[(sub[i], suffix)] = prev
                prev = suffix
    return reductions

def replacements(molecule, rules):
    # m = A y B z
    #
    # replace(m,A=>s) = s y B z
    # replace(m,B=>t) = A y t z
    #
    # For a replacement A=>s and a later replacement B=>t to have the same result we must have:
    #
    # s y B = A y t
    #
    # s[0] = A
    # t[-1] = B
    #
    # s[1:] y = y t[:-1]
    #
    # TODO: determine exactly what the substring y can look like, then only count replacements if a later replacement wouldn't result in the same string.
    #
    res = set()
    for i, atom, in enumerate(molecule):
        for sub in rules[atom]:
            res.add(''.join(molecule[:i] + sub + molecule[i+1:]))
    return len(res)

def reduce_fast(molecule, rules):
    counts = Counter(molecule)
    # All rules are of the form:
    #
    # 1. Y => X X
    # 2. Y => X 'Rn' X ('Y' X)* 'Ar'
    #
    # In the first case each application reduces the length by 1, so there are len(molecule)-1 reductions needed in total.
    # The second case is equivalent to the first if 'Rn', 'Ar' and the pairs of ('Y' X) are ignored.
    #
    return len(molecule) - counts['Rn'] - counts['Ar'] - 2*counts['Y'] - 1

def reduce(molecule, rules):
    reductions = reverse(rules)
    @cache
    def recur(start, stop):
        # For a given substring, return all the possible reductions (to a single atom) together with the minimum step count.
        if stop - start == 1:
            return { molecule[start]: 0 }
        res = {}
        for i in range(start + 1, stop):
            for A, steps1 in recur(start, i).items():
                for B, steps2 in recur(i, stop).items():
                    if (A, B) in reductions:
                        S = reductions[(A, B)]
                        res[S] = min(res.get(S, inf), steps1 + steps2 + (1 if S in rules else 0))
        return res
    return min(recur(0, len(molecule)).values())

chunks = get_input(19).split('\n\n')
rules = parse_rules(chunks[0])
molecule = parse_molecule(chunks[1])

print('1.', replacements(molecule, rules))
print('2.', reduce_fast(molecule, rules))
