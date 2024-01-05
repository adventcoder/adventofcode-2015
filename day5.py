import re
from utils import get_input

def nice(s):
    return re.search(r'[aeiou].*[aeiou].*[aeiou]', s) and re.search(r'([a-z])\1', s) and not re.search(r'ab|cd|pq|xy', s)

def better_nice(s):
    return re.search(r'([a-z][a-z]).*\1', s) and re.search(r'([a-z])[a-z]\1', s)

strings = get_input(5).splitlines()
print('1.', sum(1 if nice(s) else 0 for s in strings))
print('2.', sum(1 if better_nice(s) else 0 for s in strings))
