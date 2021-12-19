# minX = 20
# maxX = 30
# minY = -10
# maxY = -5

minX = 135
maxX = 155
minY = -102
maxY = -78

def ycount(y):
    step = 1
    steps = []
    deltay = y - 1

    while y > maxY:
        y = y + deltay
        deltay -= 1
        step += 1

    while y >= minY:
        steps.append(step)
        y = y + deltay
        deltay -= 1
        step += 1

    return steps

def xcount(x, ysteps):
    step = 1
    deltax = x - 1

    while x < minX and step <= max(ysteps):
        if deltax > 0:
            x += deltax
            deltax -= 1
        step += 1

    if x >= minX:
        while x <= maxX and step <= max(ysteps):
            if step in ysteps:
                return 1
            if deltax > 0:
                x += deltax
                deltax -= 1
            step += 1

    return 0

total = 0

for y in range(minY, abs(minY)):
    steps = ycount(y)

    if len(steps) > 0:
        for x in range(6, maxX + 1):
            total += xcount(x, steps)
print(total)
