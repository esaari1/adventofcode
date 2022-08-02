insts = ['cpy 41 a',
'inc a',
'inc a',
'dec a',
'jnz a 2',
'dec a']


insts = ['cpy 1 a',
'cpy 1 b',
'cpy 26 d',
'jnz c 2',
'jnz 1 5',
'cpy 7 c',
'inc d',
'dec c',
'jnz c -2',
'cpy a c',
'inc a',
'dec b',
'jnz b -2',
'cpy c b',
'dec d',
'jnz d -6',
'cpy 19 c',
'cpy 14 d',
'inc a',
'dec d',
'jnz d -2',
'dec c',
'jnz c -5']

reg = {
    'a': 0,
    'b': 0,
    'c': 1,
    'd': 0
}

pos = 0

while pos < len(insts):
    p = insts[pos].split()

    if p[0] == 'cpy':
        if p[1] in reg:
            reg[p[2]] = reg[p[1]]
        else:
            reg[p[2]] = int(p[1])
        pos += 1

    elif p[0] == 'inc':
        reg[p[1]] += 1
        pos += 1

    elif p[0] == 'dec':
        reg[p[1]] -= 1
        pos += 1

    elif p[0] == 'jnz':
        #print(insts[pos])
        val = p[1]
        if p[1] in reg:
            val = reg[val]

        if val != 0:
            pos += int(p[2])
        else:
            pos += 1

print(reg['a'])