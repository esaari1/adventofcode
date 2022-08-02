insts = [
'cpy 2 a',
'tgl a',
'tgl a',
'tgl a',
'cpy 1 a',
'dec a',
'dec a'
]

insts = [
'cpy a b',
'dec b',
'cpy a d',
'cpy 0 a',
'mul a b d',
'cpy 0 c',
'cpy 0 d',
'nop',
'nop',
'nop',
'dec b',
'cpy b c',
'cpy c d',
'dec d',
'inc c',
'jnz d -2',
'tgl c',
'cpy -16 c',
'jnz 1 c',
'cpy 90 c',
'jnz 90 d',
'inc a',
'inc d',
'jnz d -2',
'inc c',
'jnz c -5'
]

pos = 0

reg = {
    'a': 12,
    'b': 0,
    'c': 0,
    'd': 0
}

def toggle(loc):
    if loc >= len(insts):
        return

    p = insts[loc].split()

    if len(p) == 2:
        if p[0] == 'inc':
            insts[loc] = 'dec ' + p[1]
        else:
            insts[loc] = 'inc ' + p[1]

    elif p[0] == 'jnz':
        insts[loc] = f'cpy {p[1]} {p[2]}'

    else:
        insts[loc] = f'jnz {p[1]} {p[2]}'


while pos < len(insts):
    p = insts[pos].split()

    if p[0] == 'cpy':
        if p[2] in reg:
            if p[1] in reg:
                reg[p[2]] = reg[p[1]]
            else:
                reg[p[2]] = int(p[1])
        pos += 1

    elif p[0] == 'inc':
        if p[1] in reg:
            reg[p[1]] += 1
        pos += 1

    elif p[0] == 'mul':
        if p[1] in reg:
            a1 = p[2]
            if a1 in reg:
                a1 = reg[a1]
            a2 = p[3]
            if a2 in reg:
                a2 = reg[a2]
            reg[p[1]] = int(a1) * int(a2)
        pos += 1

    elif p[0] == 'dec':
        if p[1] in reg:
            reg[p[1]] -= 1
        pos += 1

    elif p[0] == 'jnz':
        val = p[1]
        dist = p[2]

        if p[1] in reg:
            val = reg[val]

        if p[2] in reg:
            dist = reg[dist]

        if val != 0:
            pos += int(dist)
        else:
            pos += 1

    elif p[0] == 'tgl':
        val = p[1]
        if p[1] in reg:
            val = reg[val]

        toggle(pos + val)
        pos += 1

    elif p[0] == 'nop':
        pos += 1

print(reg['a'])