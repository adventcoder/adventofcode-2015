from utils import get_input

step_map = { '(': 1, ')': -1 }
floors = [0]
for step in get_input(1):
    floors.append(floors[-1] + step_map[step])

print('1.', floors[-1])
print('2.', next(i for i, floor in enumerate(floors) if floor < 0))
