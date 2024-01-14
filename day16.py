from utils import get_input, tabulate

def parse_sue(s):
    return { lval.strip(): int(rval) for lval, rval in tabulate(s, ':', ',', maxsplit=1) }

def matches(sue, target, k):
    if k in ('cats', 'trees'):
        return sue[k] > target[k]
    if k in ('pomeranians', 'goldfish'):
        return sue[k] < target[k]
    return sue[k] == target[k]

target = parse_sue('children: 3, cats: 7, samoyeds: 2, pomeranians: 3, akitas: 0, vizslas: 0, goldfish: 5, trees: 3, cars: 2, perfumes: 1')

sues = [(int(lval.split()[-1]), parse_sue(rval)) for lval, rval in tabulate(get_input(16), ':', maxsplit=1)]

print('1.', next(num for num, sue in sues if all(sue[k] == target[k] for k in sue)))
print('2.', next(num for num, sue in sues if all(matches(sue, target, k) for k in sue)))
