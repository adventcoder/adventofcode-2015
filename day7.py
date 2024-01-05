from utils import get_input

class Wire:
    def __init__(self, expr):
        self.expr = expr
        self.signal = None

    def getsignal(self):
        if self.signal is None:
            self.signal = eval(self.expr)
        return self.signal

def eval(expr):
    match expr:
        case [x]:
            return signal(x)
        case ['NOT', x]:
            return signal(x) ^ 0xFFFF
        case [x, 'AND', y]:
            return signal(x) & signal(y)
        case [x, 'OR', y]:
            return signal(x) | signal(y)
        case [x, 'LSHIFT', y]:
            return (signal(x) << signal(y)) & 0xFFFF
        case [x, 'RSHIFT', y]:
            return signal(x) >> signal(y)

def signal(name):
    return int(name) if name.isdigit() else wires[name].getsignal()

wires = {}
for line in get_input(7).splitlines():
    rval, lval = line.split(' -> ')
    wires[lval] = Wire(rval.split())

prev_signal = signal('a')
print('1.', prev_signal)

for wire in wires.values():
    wire.signal = None
wires['b'].signal = prev_signal

print('2.', signal('a'))
