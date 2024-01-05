import numpy as np
from utils import get_input

#TODO: do this with boolean operations on rectilinear polygonal regions

grid1 = np.zeros((1000, 1000), dtype=np.uint8)
grid2 = np.zeros((1000, 1000), dtype=np.int16)

for line in get_input(6).splitlines():
    tokens = line.split()
    x1, y1 = (int(s)     for s in tokens[-3].split(','))
    x2, y2 = (int(s) + 1 for s in tokens[-1].split(','))
    if tokens[:2] == ['turn', 'on']:
        grid1[x1:x2, y1:y2] = 1
        grid2[x1:x2, y1:y2] += 1
    elif tokens[:2] == ['turn', 'off']:
        grid1[x1:x2, y1:y2] = 0
        grid2[x1:x2, y1:y2] = np.maximum(grid2[x1:x2, y1:y2] - 1, 0)
    elif tokens[0] == 'toggle':
        grid1[x1:x2, y1:y2] ^= np.ones((x2-x1, y2-y1), dtype=np.uint8)
        grid2[x1:x2, y1:y2] += 2

print('1.', np.sum(grid1))
print('2.', np.sum(grid2))