from utils import get_input
from functools import cache

ns = sorted(map(int, get_input(17).splitlines()), reverse=True)

remaining = [sum(ns)]
for n in ns:
    remaining.append(remaining[-1] - n)

@cache
def count_ways(target, i=0):
    if target == 0:
        return { 0: 1 } # 1 way using 0 buckets
    if target > remaining[i]:
        return {}
    # get ways not using bucket i
    ways = count_ways(target, i + 1).copy()
    # add ways using bucket i
    if ns[i] <= target:
        for buckets, count in count_ways(target - ns[i], i + 1).items():
            ways[buckets + 1] = ways.get(buckets + 1, 0) + count
    return ways

ways = count_ways(150)
print('1.', sum(ways.values()))
print('2.', ways[min(ways.keys())])
