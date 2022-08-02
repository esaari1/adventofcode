from collections import deque

vals = list(range(256))
s = '83,0,193,1,254,237,187,40,88,27,2,255,149,29,42,100'

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

print(ans)
