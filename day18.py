from utils import get_input
from collections import Counter

width = 100
height = 100

def coord(x, y):
    return x + y*(width + 2)

def valid(p):
    x, y = divmod(p, width + 2)
    return 0 <= x < width and 0 <= y < height

dirs = [coord(x, y) for y in (-1, 0, 1) for x in (-1, 0, 1) if (x, y) != (0, 0)]

def parse_state(s):
    return set(coord(x, y) for y, line in enumerate(s.splitlines()) for x, c in enumerate(line) if c == '#')

def update(state):
    counts = Counter(p + d for p in state for d in dirs)
    return set(p for p, count in counts.items() if (p in state and 2 <= count <= 3) or (p not in state and count == 3 and valid(p)))

corners = [coord(0, 0), coord(width - 1, 0), coord(0, height - 1), coord(width - 1, height - 1)]
state1 = parse_state(get_input(18))
state2 = state1.copy()
state2.update(corners)
for _ in range(100):
    state1 = update(state1)
    state2 = update(state2)
    state2.update(corners)
print('1.', len(state1))
print('2.', len(state2))
