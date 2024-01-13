from utils import get_input

steps = get_input(3)
step_map = { '>': 1, 'v': 1j, '<': -1, '^': -1j }

def visit(steps):
    seen = set()
    pos = 0
    seen.add(pos)
    for step in steps:
        pos += step_map[step]
        seen.add(pos)
    return seen

print('1.', len(visit(steps)))
print('2.', len(visit(steps[0::2]) | visit(steps[1::2])))
