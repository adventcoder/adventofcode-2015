from utils import get_input, Interval
from math import inf
from functools import cache

def parse_matrix(input, size):
    matrix = [[inf] * size for _ in range(size)]
    lines = iter(input.splitlines())
    for i in range(size):
        for j in range(i + 1, size):
            tokens = next(lines).split()
            matrix[i][j] = int(tokens[-1])
            matrix[j][i] = matrix[i][j]
    return matrix

def find_best_route(matrix):
    mask = (1 << len(matrix)) - 1

    @cache
    def visit(i, visited=0):
        visited |= 1 << i
        if visited == mask:
            return Interval(0, 0)
        best = Interval(inf, -inf)
        for j in range(len(matrix)):
            if not visited & (1 << j):
                best |= visit(j, visited) + matrix[i][j]
        return best

    best = Interval(inf, -inf)
    for start in range(len(matrix)):
        best |= visit(start)
    return best

route = find_best_route(parse_matrix(get_input(9), 8))
print('1.', route.min)
print('2.', route.max)
