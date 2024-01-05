from utils import get_input, Interval, union
from math import inf
from functools import cache

N = 8
mask = (1 << N) - 1
dist = [[inf] * N for _ in range(N)]
lines = get_input(9).splitlines()
for i in range(N):
    for j in range(i + 1, N):
        tokens = lines.pop(0).split()
        d = int(tokens[-1])
        dist[i][j] = d
        dist[j][i] = d

@cache
def find_best_route(i, visited=0):
    visited |= 1 << i
    if visited == mask:
        return Interval(0, 0)
    best = Interval(inf, -inf)
    for j in range(8):
        if not visited & (1 << j):
            best |= find_best_route(j, visited) + dist[i][j]
    return best

route = union(find_best_route(start) for start in range(N))
print('1.', route.min)
print('2.', route.max)
