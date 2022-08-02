import numpy

a = 312051

def part1():
    i = 1
    m = 8
    ring = 1
    plast = 1
    sidel = 2
    while i < a:
        i += m
        m += 8
        ring += 1
        sidel += 2

    m = m - 8
    ring = ring - 1
    sidel -= 2

    rfirst = i - m + 1

    s = 0
    sideEnd = rfirst + sidel - 1

    while sideEnd < a:
        s += 1
        sideEnd += sidel

    mid = int((sideEnd + (sideEnd - sidel)) / 2)

    ans = ring + abs(mid - a)
    print(ans)

n = numpy.zeros((500, 500), dtype=int)

n[(250, 250)] = 1

sidel = 2
side = 0
pos = (251, 251)

while True:
    while side < 4:
        i = 0

        while i < sidel:
            if side == 0:
                pos = (pos[0]-1, pos[1])
            elif side == 1:
                pos = (pos[0], pos[1]-1)
            elif side == 2:
                pos = (pos[0]+1, pos[1])
            elif side == 3:
                pos = (pos[0], pos[1]+1)

            sub = n[pos[0]-1:pos[0]+2, pos[1]-1:pos[1]+2]
            n[pos] = sub.sum()

            if n[pos] > a:
                print(n[pos])
                exit(0)

            i += 1

        side += 1

    sidel += 2
    pos = (pos[0] +1, pos[0]+1)
    side = 0