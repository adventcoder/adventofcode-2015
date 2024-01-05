from utils import get_input
from ast import literal_eval

def literal_len(s):
    return len(s) + s.count('\\') + s.count('"') + 2

strs = get_input(8).splitlines()
print('1.', sum(len(s) - len(literal_eval(s)) for s in strs))
print('2.', sum(literal_len(s) - len(s) for s in strs))
