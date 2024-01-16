from utils import get_input

def parse_sue(s):
    sue = {}
    for line in s.split(','):
        lval, rval = line.split(':', maxsplit=1)
        sue[lval.strip()] = int(rval)
    return sue

def matches(sue, target, k):
    if k in ('cats', 'trees'):
        return sue[k] > target[k]
    if k in ('pomeranians', 'goldfish'):
        return sue[k] < target[k]
    return sue[k] == target[k]

target = parse_sue('children: 3, cats: 7, samoyeds: 2, pomeranians: 3, akitas: 0, vizslas: 0, goldfish: 5, trees: 3, cars: 2, perfumes: 1')

sues = []
for line in get_input(16).splitlines():
    lval, rval = line.split(':', maxsplit=1)
    sues.append((int(lval.split()[-1]), parse_sue(rval)))

print('1.', next(num for num, sue in sues if all(sue[k] == target[k] for k in sue)))
print('2.', next(num for num, sue in sues if all(matches(sue, target, k) for k in sue)))
