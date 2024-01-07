from utils import get_input
from functools import cache
from math import inf

def parse_matrix(input, size):
    matrix = [[0] * size for _ in range(size)]
    lines = iter(input.splitlines())
    for i in range(size):
        for j in range(size):
            if i != j:
                tokens = next(lines).split()
                modifier = { 'gain': 1, 'lose': -1 }[tokens[2]]
                matrix[i][j] = int(tokens[3]) * modifier
    return matrix

def find_maximum_happiness(matrix):
    mask = (1 << len(matrix)) - 1
    fixed = len(matrix) - 1 # fix any one of the guests to an arbitraty position

    @cache
    def sit(i, seated=0): # i: next guest to sit, seated: guests already seated
        seated |= 1 << i
        if seated == mask:
            return matrix[fixed][i] + matrix[i][fixed]
        happiness = -inf
        for j in range(len(matrix)):
            if not seated & (1 << j):
                happiness = max(happiness, sit(j, seated) + matrix[i][j] + matrix[j][i])
        return happiness

    return sit(fixed)

matrix = parse_matrix(get_input(13), 8)

print('1.', find_maximum_happiness(matrix))

for row in matrix:
    row.append(0)
matrix.append([0] * len(matrix) + [0])

print('2.', find_maximum_happiness(matrix))
