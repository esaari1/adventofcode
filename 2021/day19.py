# positive X left
# positive Y up
# positive Z towards me

def rotateX(scanner):
    rotated = []
    for coord in scanner:
        rotated.append((coord[0], coord[2], -coord[1]))
    return rotated

def rotateY(scanner):
    rotated = []
    for coord in scanner:
        rotated.append((coord[2], coord[1], -coord[0]))
    return rotated

def rotateZ(scanner):
    rotated = []
    for coord in scanner:
        rotated.append((-coord[1], coord[0], coord[2]))
    return rotated

def scan(s1, s2):
    for s1item in s1:
        for s2item in s2:
            dx = s2item[0] - s1item[0]
            dy = s2item[1] - s1item[1]
            dz = s2item[2] - s1item[2]

            count = 0
            match = []
            for item in s2:
                t = (item[0] - dx, item[1] - dy, item[2] - dz)
                match.append(t)
                if t in smap:
                    count += 1

            if count >= 12:
                return match, (dx, dy, dz)

    return None, None


def compare(s1, s2):
    for y in range(4):
        for z in range(4):
            (a, delta) = scan(s1, s2)
            if a is not None:
                return a, delta
            s2 = rotateZ(s2)
        s2 = rotateY(s2)

    s2 = rotateX(s2)
    for y in range(4):
        for z in range(4):
            (a, delta) = scan(s1, s2)
            if a is not None:
                return a, delta
            s2 = rotateZ(s2)
        s2 = rotateY(s2)

    s2 = rotateX(s2)
    s2 = rotateX(s2)
    for y in range(4):
        for z in range(4):
            (a, delta) = scan(s1, s2)
            if a is not None:
                return a, delta
            s2 = rotateZ(s2)
        s2 = rotateY(s2)

    return None, None

f = open('input.txt')

line = f.readline()

scanners = []
scannerRanges = []

scanner = None
minX = 1000
maxX = -1000
minY = 1000
maxY = -1000
minZ = 1000
maxZ = -1000

while line:
    line = line.strip()

    if line == '':
        scanner.sort()
        scanners.append(scanner)
        scannerRanges.append(((minX, maxX), (minY, maxY), (minZ, maxZ)))
        minX = 1000
        maxX = -1000
        minY = 1000
        maxY = -1000
        minZ = 1000
        maxZ = -1000


    elif line[0:3] == '---':
        scanner = []

    else:
        (x, y, z) = [int(x) for x in line.split(',')]
        scanner.append((x, y, z))

    line = f.readline()

f.close()

def part2():
    # part1 = [(0, 0, 0), (-68, 1246, 43), (92, 2380, 20), (20, 1133, -1061), (-1105, 1205, -1229)]
    part1 = [(0, 0, 0), (-30, -1285, 142), (-42, -1301, 1267), (74, 1191, 81), (-1220, -1180, 13), (1187, -1312, 1285), (-29, -132, -1191), (90, -2565, 172), (2419, -1273, 1219), (1242, -140, 1263), (1336, -1359, 77), (2436, -1259, 173), (-10, -2501, 1246), (-1230, -2417, 1372), (2422, -2548, 1281), (-1122, -119, -1067), (17, -3764, 44), (-1208, -2390, 2397), (-1149, -2468, -20), (1228, -2561, 2446), (1208, -3739, 2527), (-1061, -73, -2300), (-2401, -2528, 2424), (1239, -2402, 3771), (-2388, -100, -1159), (42, -2452, 2382), (-38, -3657, 2562), (-3, -2528, 3619), (-1135, -3637, 1300), (85, -3746, 1193), (2342, -2492, 2471), (3617, -2549, 2451), (1196, -3690, 1201), (34, -4891, 1247), (-1152, -3586, -16), (-1212, -2556, 3648), (-1162, -2503, 4876), (-44, -5995, 1208), (3587, -2468, 3682), (-12, -7242, 1248)]

    dist = 0
    for i in range(len(part1) - 1):
        for j in range(i+1, len(part1)):
            p1 = part1[i]
            p2 = part1[j]
            a = abs(p2[0] - p1[0]) + abs(p2[1] - p1[1]) + abs(p2[2] - p1[2])
            if a == 3621:
                print(p1, p2)
            if a > dist:
                dist = a

    print(dist)


def part1():
    scannerRanges.append(((minX, maxX), (minY, maxY), (minZ, maxZ)))

    spos = [(0, 0, 0)]
    scanner.sort()
    scanners.append(scanner)

    s0 = scanners[0]
    smap = {}
    for item in s0:
        smap[item] = True

    matches = [0]
    while len(matches) < len(scanners):
        for i in range(1, len(scanners)):
            if i not in matches:
                print('CHECK', i)
                (a, delta) = compare(s0, scanners[i])
                if a is not None:
                    print(i)
                    spos.append(delta)
                    matches.append(i)
                    for item in a:
                        if item not in smap:
                            smap[item] = True
                            s0.append(item)

                    s0.sort()

    print(len(s0))
    print(spos)

# part1()
part2()
