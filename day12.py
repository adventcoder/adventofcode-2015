from utils import get_input, ints
import json

def total(obj):
    if type(obj) == dict:
        return 0 if 'red' in obj.values() else sum(map(total, obj.values()))
    elif type(obj) == list:
        return sum(map(total, obj))
    elif type(obj) == int:
        return obj
    else:
        return 0

s = get_input(12)
print('1.', sum(ints(s)))
print('2.', total(json.loads(s)))
