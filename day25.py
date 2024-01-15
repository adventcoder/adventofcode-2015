from utils import get_input, ints

def code(r, c):
    n = (r+c)*(r+c-1)//2 - r
    m = 33554393
    a = 20151125
    b = 252533
    while n > 0:
        if n % 2 == 1:
            a = (a * b) % m
        b = (b * b) % m
        n //= 2
    return a

r, c = ints(get_input(25))
print('1.', code(r, c))
