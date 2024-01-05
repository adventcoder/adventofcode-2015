from utils import get_input, slices, iterate
import re

def step(pwd):
    i = -1
    while pwd[i] == 'z':
        i -= 1
    return pwd[:i] + chr(ord(pwd[i]) + 1) + 'a'*(-i-1)

def valid(pwd):
    return not confusing(pwd) and straight(pwd) and pairs(pwd)

def confusing(pwd):
    return any(c in 'iol' for c in pwd)

def straight(pwd):
    return any(ord(b) == ord(a) + 1 and ord(c) == ord(b) + 1 for a, b, c in slices(pwd, 3, overlap=True))

def pairs(pwd):
    return len(set(re.findall(r'([a-z])\1', pwd))) >= 2

pwds = filter(valid, iterate(step, get_input(11).strip()))
print('1.', next(pwds))
print('2.', next(pwds))
