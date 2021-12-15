import numpy as np

a = np.zeros((1000, 1000), dtype=int)

with open('input.txt') as readfile:
    for line in readfile:
        (p1, p2) = line.strip().split(' -> ')
        (x1, y1) = p1.split(',')
        (x2, y2) = p2.split(',')

        x1 = int(x1)
        y1 = int(y1)
        x2 = int(x2)
        y2 = int(y2)

        if x1 == x2:
            if y1 > y2:
                a[y2:y1+1, x1] += 1
            else:
                a[y1:y2+1, x1] += 1

        elif y1 == y2:
            if x1 > x2:
                a[y1, x2:x1+1] += 1
            else:
                a[y1, x1:x2+1] += 1

        else:
            dx = abs(x1 - x2)
            dy = abs(y1 - y2)

            if dx == dy:
                if x1 < x2:
                    if y1 < y2:
                        for x in range(dx+1):
                            a[y1, x1] += 1
                            x1 += 1
                            y1 += 1

                    else:
                        for x in range(dx+1):
                            a[y1, x1] += 1
                            x1 += 1
                            y1 -= 1

                else:
                    if y1 < y2:
                        for x in range(dx+1):
                            a[y1, x1] += 1
                            x1 -= 1
                            y1 += 1

                    else:
                        for x in range(dx+1):
                            a[y1, x1] += 1
                            x1 -= 1
                            y1 -= 1

print(a)
print(len(np.where(a > 1)[0]))
