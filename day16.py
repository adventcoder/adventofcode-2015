from utils import get_input

def parse_props(s):
    props = {}
    for chunk in s.split(','):
        lval, rval = chunk.split(':', 1)
        props[lval.strip()] = int(rval)
    return props

def matches(props, target, k):
    if k in ('cats', 'trees'):
        return props[k] > target[k]
    if k in ('pomeranians', 'goldfish'):
        return props[k] < target[k]
    return props[k] == target[k]

target = parse_props('children: 3, cats: 7, samoyeds: 2, pomeranians: 3, akitas: 0, vizslas: 0, goldfish: 5, trees: 3, cars: 2, perfumes: 1')

sues = []
for line in get_input(16).splitlines():
    lval, rval = line.split(':', 1)
    num = int(lval.split()[-1])
    sues.append((num, parse_props(rval)))

print('1.', next(num for num, props in sues if all(props[k] == target[k] for k in props)))
print('2.', next(num for num, props in sues if all(matches(props, target, k) for k in props)))
