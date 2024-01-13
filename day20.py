from utils import get_input
from math import *

gamma = 0.5772156649015329
exp_gamma = 1.781072417990198

def find_root(f, x1, x2):
    # Finds (floor(x), ceil(x)) where f(x)==0
    while x2 - x1 > 1:
        x = (x1 + x2) / 2
        y = f(x)
        if y <= 0:
            x1 = floor(x)
        if y >= 0:
            x2 = ceil(x)
    return x1, x2

def find_house1(target, factor):
    #
    # P(n) = 10 sigma(n)
    #
    # For an upper bound on the number of presents use Robin's inequality:
    #
    # sigma(n) <= 10 e^γ n log(log(n))
    #
    # The lower bound is derived from Robin's inequality applied to sigma(Pn#), since n must be a highly abundant number which is at as good as a primorial.
    #
    # Pn# ~ n e^n => sigma(n) >= e^γ n log(W(n))
    #
    # W(n) = log(n) - log(W(n)) = log(n) - log(log(n) - ...)
    #
    _, upper = find_root(lambda n: factor*exp_gamma*n*log(log(n) - log(log(n))) - target, 1, target)
    lower, _ = find_root(lambda n: factor*exp_gamma*n*log(log(n)) - target, 5041, upper)
    houses = [0] * (upper - lower + 1)
    d = 1
    while d*d <= upper:
        for k in range(-((-lower)//d), (upper//d) + 1):
            houses[k*d-lower] += d + k
        d += 1
    return next(n for n in range(lower, upper+1) if factor*houses[n-lower] >= target)

def find_house2(target, factor, visits):
    # P(n) = 11 sum(d for d in divisors(n) if n<=d*50)
    #      = 11 n sum(1/d for d in divisors(n) if d<=50)
    #      <= 11 n sum(1/d for d in range(1, 50+1))
    #      <= 11 n (log(50+1) + γ)
    #      <= 49.5995 n
    #
    upper = ceil(target/factor) # better bound?
    lower = floor(target/(factor*(log(visits+1) + gamma)))
    houses = [0] * (upper - lower + 1)
    for d in range(1, visits + 1):
        for k in range(-((-lower)//d), (upper//d) + 1):
            houses[k*d-lower] += k
    return next(n for n in range(lower, upper+1) if factor*houses[n-lower] >= target)

target = int(get_input(20))
print('1.', find_house1(target, 10))
print('2.', find_house2(target, 11, 50))
