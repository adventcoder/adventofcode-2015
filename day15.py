from utils import get_input, ints
import numpy as np

ingredients = np.array([list(ints(line)) for line in get_input(15).splitlines()])

def partition(n, m):
    if m == 1:
        yield (n,)
    else:
        for a in range(n + 1):
            for bs in partition(n - a, m - 1):
                yield (a, *bs)

#TODO: derive bounds and restrict loop to where score terms are all positive https://en.wikipedia.org/wiki/Fourier%E2%80%93Motzkin_elimination

best_score1 = 0
best_score2 = 0
for weights in partition(100, len(ingredients)):
    cap, dur, fla, tex, cal = np.dot(np.transpose(ingredients), weights)
    score = max(cap, 0)*max(dur, 0)*max(fla, 0)*max(tex, 0)
    best_score1 = max(best_score1, score)
    if cal == 500:
        best_score2 = max(best_score2, score)
print('1.', best_score1)
print('2.', best_score2)
