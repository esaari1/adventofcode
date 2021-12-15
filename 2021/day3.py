import itertools

def process(vals):
    global zeros
    global ones
    zeros = [0] * len(vals[0])
    ones = [0] * len(vals[0])

    for v in vals:
        idx = 0
        for c in v:
            if c == '0':
                zeros[idx] += 1
            else:
                ones[idx] += 1
            idx += 1

f = open('input.txt')

zeros = []
ones = []
vals = []

line = f.readline()

while line:
    vals.append(line.strip())
    line = f.readline()


def part1():
    gamma = ''
    epssilon = ''
    process(vals)

    for x in range(len(zeros)):
        if zeros[x] > ones[x]:
            gamma += '0'
            epssilon += '1'
        else:
            gamma += '1'
            epssilon += '0'

    gamma = int(gamma, 2)
    epssilon = int(epssilon, 2)
    print(gamma * epssilon)

#part1()

origVals = vals[:]
process(vals)

for x in range(len(zeros)):
    ox = [1] * len(vals)
    if zeros[x] > ones[x]:
        for idx in range(len(vals)):
            if vals[idx][x] == '1':
                ox[idx] = 0
    else:
        for idx in range(len(vals)):
            if vals[idx][x] == '0':
                ox[idx] = 0

    print(ox)
    it = itertools.compress(vals, ox)
    vals = []
    for i in it:
        vals.append(i)
    print(vals)
    if (len(vals)) == 1:
        break
    process(vals)

o = int(vals[0], 2)
vals = origVals[:]

process(vals)

for x in range(len(zeros)):
    co2 = [1] * len(vals)
    if ones[x] > zeros[x]:
        for idx in range(len(vals)):
            if vals[idx][x] == '1':
                co2[idx] = 0
    elif ones[x] < zeros[x]:
        for idx in range(len(vals)):
            if vals[idx][x] == '0':
                co2[idx] = 0

    else:
        for idx in range(len(vals)):
            if vals[idx][x] == '1':
                co2[idx] = 0


    print(co2)
    it = itertools.compress(vals, co2)
    vals = []
    for i in it:
        vals.append(i)
    print(vals)
    if (len(vals)) == 1:
        break
    process(vals)

c = int(vals[0], 2)

print(o * c)

