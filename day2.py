from utils import get_input

paper = 0
ribbon = 0

for line in get_input(2).splitlines():
    l, w, h = map(int, line.split('x'))
    paper += 2*(l*w + w*h + h*l) + min(l*w, w*h, h*l)
    ribbon += 2*min(l+w, w+h, h+l) + l*w*h

print('1.', paper)
print('2.', ribbon)
