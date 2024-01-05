import hashlib
from utils import get_input

secret = get_input(4)

def hash(n):
    return hashlib.md5(bytes(secret + str(n), 'ascii')).hexdigest()

n = 1
while not hash(n).startswith('00000'):
    n += 1
print('1.', n)
while not hash(n).startswith('000000'):
    n += 1
print('2.', n)
