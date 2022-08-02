s = {}

def getCount(program):
    count = 1

    for p in programs[program]:
        if p not in s:
            s[p] = True
            count += getCount(p)

    return count

def expand(program):
    s[program] = True

    for p in programs[program]:
        if p not in s:
            s[p] = True
            expand(p)

f = open('input.txt')

line = f.readline()
programs = {}

while line:
    (p1, plist) = line.strip().split(' <-> ')

    programs[p1] = []
    for p in plist.split(', '):
        programs[p1].append(p)

        if p not in programs:
            programs[p] = []

        if p1 not in programs[p]:
            programs[p].append(p1)

    line = f.readline()

f.close()

def part1():
    s['0'] = True
    print(getCount('0'))

# part2
count = 0
for program in programs:
    if program not in s:
        expand(program)
        count += 1

print(count)
