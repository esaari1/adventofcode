from collections import deque
import numpy as np
from skimage import measure

input = 'flqrgnkx'
input = 'hwlqcszp'

def process(i):
    vals = list(range(256))
    s = f'{input}-{i}'

    lengths = []
    for c in s:
        lengths.append(ord(c))

    lengths = lengths + [17,31,73,47,23]
    pos = 0
    step = 0

    for x in range(64):
        for l in lengths:
            d = deque(vals)
            d.rotate(-pos)
            vals = list(d)

            r = vals[:l]
            r.reverse()
            vals = r + vals[l:]

            d = deque(vals)
            d.rotate(pos)
            vals = list(d)

            pos = pos + l + step
            step += 1

    ans = ''
    pos = 0
    for x in range(16):
        d = vals[16 * x]

        for y in range(15):
            d = d ^ vals[16 * x + y + 1]

        s = format(d, 'x')
        if len(s) == 1:
            ans += '0'
        ans += str(s)

    return ans

a = np.zeros((128, 128))
for x in range(128):
    ans = process(x)
    bits = str(bin(int(ans, 16))[2:])

    bits = [int(x) for x in ','.join(bits).split(',')]

    l = [0] * (128 - len(bits))
    bits = l + bits

    a[x] = bits

print(len(np.where(a == 1)[0]))

img_labeled = measure.label(a, connectivity=1)
print(np.amax(img_labeled))
