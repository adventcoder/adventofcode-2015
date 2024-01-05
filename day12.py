from utils import get_input
import json
import re

s = get_input(12)
print('1.', sum(map(int, re.findall(r'-?[0-9]+', s))))

def total(obj):
    if type(obj) == dict:
        return 0 if 'red' in obj.values() else sum(map(total, obj.values()))
    elif type(obj) == list:
        return sum(map(total, obj))
    elif type(obj) == int:
        return obj
    else:
        return 0

print('2.', total(json.loads(s)))
