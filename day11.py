from utils import get_input
import re

def next_password(pwd):
    while True:
        pwd = step(pwd)
        if not confusing(pwd) and straight(pwd) and pairs(pwd):
            return pwd

def step(pwd):
    i = -1
    while pwd[i] == 'z':
        i -= 1
    return pwd[:i] + chr(ord(pwd[i]) + 1) + 'a'*(-i-1)

def confusing(pwd):
    return any(c in 'iol' for c in pwd)

def straight(pwd):
    return any(ord(pwd[i]) == ord(pwd[i + 1]) - 1 == ord(pwd[i + 2]) - 2 for i in range(len(pwd) - 2))

def pairs(pwd):
    return len(set(re.findall(r'([a-z])\1', pwd))) >= 2

pwd = get_input(11).strip()
pwd = next_password(pwd)
print('1.', pwd)
pwd = next_password(pwd)
print('2.', pwd)
