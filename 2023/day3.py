import math

valm = {}
gears = []
symbols = []
gearcount = {}

def includeKey(key):
    lval = len(valm[key])

    for dx in range(key[0] - 1, key[0] + lval + 1):
        for dy in range(key[1] - 1, key[1] + 2):
            if (dx, dy) in symbols:
                return (dx, dy)
    return None

y = 0
with open('input.txt') as f:
    val = ''
    xstart = -1
    for line in f:
        x = 0
        line = line.strip()
        for c in line:
            if c in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                val += c
                if xstart == -1:
                    xstart = x
            else:
                if len(val) > 0:
                    valm[(xstart, y)] = val
                    val = ''
                    xstart = -1
                if c != '.':
                    symbols.append((x, y))
                if c == '*':
                    gears.append((x, y))

            x += 1

        if len(val) > 0:
            valm[(xstart, y)] = val
            val = ''
            xstart = -1

        y += 1

part1 = 0
for key in valm:
    s = includeKey(key)
    if s is not None:
        part1 += int(valm[key])
        if s in gears:
            if s not in gearcount:
                gearcount[s] = []
            gearcount[s].append(int(valm[key]))

print(part1)

part2 = 0
for k in gearcount:
    if len(gearcount[k]) > 1:
        part2 += math.prod(gearcount[k])

print(part2)
