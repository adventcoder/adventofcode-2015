from utils import get_input
from collections import Counter

dirs = [complex(x, y) for y in (-1, 0, 1) for x in (-1, 0, 1) if (x, y) != (0, 0)]

def parse_state(s):
    return set(complex(x, y) for y, line in enumerate(s.splitlines()) for x, c in enumerate(line) if c == '#')

def update(state):
    counts = Counter(p + d for p in state for d in dirs)
    return set(p for p, count in counts.items() if (p in state and 2 <= count <= 3) or (p not in state and count == 3 and valid(p)))

def valid(p):
    return 0 <= p.real < 100 and 0 <= p.imag < 100

corners = [0, 99, 99j, 99+99j]
state1 = parse_state(get_input(18))
state2 = state1.copy()
state2.update(corners)
for _ in range(100):
    state1 = update(state1)
    state2 = update(state2)
    state2.update(corners)
print('1.', len(state1))
print('2.', len(state2))
