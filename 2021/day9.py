import numpy as np

found = {}

def basinSize(r, c):
    global found

    sz = 1
    found[(r, c)] = True
    if (r-1, c) not in found and arr[r-1, c] != 9:
        sz += basinSize(r-1, c)
    if (r+1, c) not in found and arr[r+1, c] != 9:
        sz += basinSize(r+1, c)
    if (r, c-1) not in found and arr[r, c-1] != 9:
        sz += basinSize(r, c-1)
    if (r, c+1) not in found and arr[r, c+1] != 9:
        sz += basinSize(r, c+1)

    return sz

arr = np.full((102, 102), 9, dtype=int)
#arr = np.full((7, 12), 9, dtype=int)

f = open('input.txt')
line = f.readline()
row = 1

while line:
    line = line.strip()
    line = f'9{line}9'
    vals = [int(c) for c in line]
    arr[row] = vals
    row += 1
    line = f.readline()

f.close()

maxr = 101
maxc = 101

# maxr = 6
# maxc = 11

sizes = []

ans = 0
for r in range(1, maxr):
    for c in range(1, maxc):
        suba = arr[r-1:r+2, c-1:c+2]

        m = min(np.min(suba[1]), np.min(suba[:,1]))
        if m == arr[r, c] and m != 9:
            found = {}
            ans += arr[r, c] + 1
            sz = basinSize(r, c)
            print(m, sz)
            sizes.append(sz)

print(ans)
sizes.sort()
ans = 1
print(sizes[-3:])
for s in sizes[-3:]:
    ans *= s

print(ans)