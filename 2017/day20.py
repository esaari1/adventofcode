points = []
vels = []
acs = []

def hash(x):
    return f'{x[0]}_{x[1]}_{x[2]}'

with open('input.txt') as f:
    line = f.readline()

    while line:
        #p=<-833,-499,-1391>, v=<84,17,61>, a=<-4,1,1>
        parts = line.strip().split(', ')

        p = parts[0][3:-1].split(',')
        p = [int(x) for x in p]
        points.append(p)

        p = parts[1][3:-1].split(',')
        p = [int(x) for x in p]
        vels.append(p)

        p = parts[2][3:-1].split(',')
        p = [int(x) for x in p]
        acs.append(p)

        line = f.readline()

print(1000)
for i in range(5000):
    pos = {}
    dups = []
    for x in range(len(points)):
        vels[x][0] += acs[x][0]
        vels[x][1] += acs[x][1]
        vels[x][2] += acs[x][2]

        points[x][0] += vels[x][0]
        points[x][1] += vels[x][1]
        points[x][2] += vels[x][2]

        key = hash(points[x])

        if key not in pos:
            pos[key] = []
        else:
            dups.append(key)
        pos[key].append(x)

    if len(dups) > 0:
        remove = []
        for key in dups:
            for idx in pos[key]:
                if idx not in remove:
                    remove.append(idx)
        remove.sort(reverse=True)

        for idx in remove:
            del points[idx]
        print(len(remove), len(points))

print(len(points))

def part1():
    dist = None
    ans = 0

    idx = 0
    for p in points:
        d = abs(p[0]) + abs(p[1]) + abs(p[2])
        if dist is None or dist > d:
            dist = d
            ans = idx
        idx += 1

    print(ans)
