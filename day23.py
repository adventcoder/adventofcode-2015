from utils import get_input

def parse(s):
    return [line.replace(',', '').split() for line in s.splitlines()]

def exec(code, a):
    reg = { 'a': a, 'b': 0 }
    ip = 0
    while ip < len(code):
        step = 1
        match code[ip]:
            case ['jmp', n]:
                step = int(n)
            case ['jie', r, n]:
                if reg[r] % 2 == 0:
                    step = int(n)
            case ['jio', r, n]:
                if reg[r] == 1:
                    step = int(n)
            case ['tpl', r]:
                reg[r] *= 3
            case ['hlf', r]:
                reg[r] //= 2
            case ['inc', r]:
                reg[r] += 1
        ip += step
    return reg['b']

def exec_fast(code, a, b=0):
    assert code[0][:2] == ['jio', 'a']
    if a == 1:
        ip = int(code[0][2])
    else:
        ip = 1
    while code[ip][0] in ('inc', 'tpl'):
        assert code[ip][1] == 'a'
        a = a + 1 if code[ip][0] == 'inc' else a * 3
        ip += 1
    while a != 1:
        b += 1
        if a % 2 == 0:
            a //= 2
        else:
            a = a*3 + 1
    return b

code = parse(get_input(23))
print('1.', exec_fast(code, 0))
print('2.', exec_fast(code, 1))
