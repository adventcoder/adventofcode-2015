from utils import get_input, ints
import numpy as np

ingredients = np.array([list(ints(line)) for line in get_input(15).splitlines()])

def partitions(n, m):
    if m == 1:
        yield (n,)
    else:
        for a in range(n + 1):
            for bs in partitions(n - a, m - 1):
                yield (a, *bs)

#TODO: derive bounds and restrict loop to where score terms are all positive

score1 = 0
score2 = 0
for weights in partitions(100, len(ingredients)):
    cap, dur, fla, tex, cal = np.dot(np.transpose(ingredients), weights)
    score = max(cap, 0)*max(dur, 0)*max(fla, 0)*max(tex, 0)
    score1 = max(score1, score)
    if cal == 500:
        score2 = max(score2, score)
print('1.', score1)
print('2.', score2)
