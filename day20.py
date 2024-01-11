from utils import get_input
import numpy as np

target = int(get_input(20))

upper = target // 10 - 1 # presents[n] >= 10*(n+1)
presents = np.zeros(upper+1)
d = 1
while d*d <= upper:
    presents[d*d] = d*10
    presents[d*d + d : upper+1 : d] += (d + np.arange(d+1, upper//d+1)) * 10
    d += 1
ns, = np.where(presents >= target)
print('1.', ns[0])

upper = target // 11 # presents[n] >= 11*n
presents = np.zeros(upper+1)
for d in range(1, 50+1):
    presents[d : upper+1 : d] += np.arange(1, upper//d+1) * 11
ns, = np.where(presents >= target)
print('2.', ns[0])
