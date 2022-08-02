from itertools import permutations
# dbfgaehc
input = ['a', 'b', 'c', 'd', 'e']
input = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']


def scramble(a):
    for line in open('input.txt'):
        parts = line.strip().split(' ')
        if parts[0] == 'swap' and parts[1] == 'position':
            pos1 = int(parts[2])
            pos2 = int(parts[5])
            a[pos1], a[pos2] = a[pos2],a[pos1]

        elif parts[0] == 'swap' and parts[1] == 'letter':
            pos1 = a.index(parts[2])
            pos2 = a.index(parts[5])
            a[pos1], a[pos2] = a[pos2],a[pos1]

        elif parts[0] == 'reverse':
            pos1 = int(parts[2])
            pos2 = int(parts[4])

            while pos1 < pos2:
                a[pos1], a[pos2] = a[pos2],a[pos1]
                pos1 += 1
                pos2 -= 1

        elif parts[0] == 'rotate' and parts[1] == 'left':
            count = int(parts[2])
            count = count % len(a)
            left = a[:count]
            a = a[count:]
            a.extend(left)

        elif parts[0] == 'rotate' and parts[1] == 'right':
            count = int(parts[2])
            count = count % len(a)
            count = len(a) - count
            left = a[:count]
            a = a[count:]
            a.extend(left)

        elif parts[0] == 'rotate' and parts[1] == 'based':
            letter = parts[6]
            pos = a.index(letter)
            count = pos + 1
            if pos >= 4:
                count += 1

            count = count % len(a)
            count = len(a) - count

            left = a[:count]
            a = a[count:]
            a.extend(left)


        elif parts[0] == 'move':
            pos1 = int(parts[2])
            pos2 = int(parts[5])
            t = a[pos1]
            a.pop(pos1)
            a.insert(pos2, t)

    return a

# part 1
a = scramble(input)
print(''.join(a))

# part 2
for p in permutations(input):
    s = scramble(list(p))
    if ''.join(s) == 'fbgdceah':
        print(''.join(p))
        exit()
