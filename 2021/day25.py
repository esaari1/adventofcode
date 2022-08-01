import numpy as np

maxr = 137
maxc = None

row = 0
with open('input.txt') as f:
    for line in f:
        line = line.strip()
        if maxc is None:
            maxc = len(line)
            arr = np.zeros((maxr, maxc), dtype=int)

        for col in range(len(line)):
            if line[col] == '>':
                arr[row, col] = 1
            elif line[col] == 'v':
                arr[row, col] = 2
        row += 1

print(arr)

moves = 0
while True:
#for x in range(10):
    print(moves)
    moved = False
    pos = np.where(arr == 1)
    newarr = np.copy(arr)

    for idx in range(len(pos[0])):
        r = pos[0][idx]
        c = pos[1][idx]
        destc = (c + 1) % maxc

        if arr[r, destc] == 0:
            moved = True
            newarr[r, c] = 0
            newarr[r, destc] = 1

    arr = np.copy(newarr)
    pos = np.where(arr == 2)
    for idx in range(len(pos[0])):
        r = pos[0][idx]
        c = pos[1][idx]
        destr = (r + 1) % maxr

        if arr[destr, c] == 0:
            moved = True
            newarr[r, c] = 0
            newarr[destr, c] = 2

    arr = newarr
    if moved:
        moves += 1
    else:
        break

print(moves+1)
#print(arr)
