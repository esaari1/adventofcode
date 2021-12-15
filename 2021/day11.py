import numpy as np

arr = np.array([(5,4,8,3,1,4,3,2,2,3),
(2,7,4,5,8,5,4,7,1,1),
(5,2,6,4,5,5,6,1,7,3),
(6,1,4,1,3,3,6,1,4,6),
(6,3,5,7,3,8,5,4,7,8),
(4,1,6,7,5,2,4,6,4,5),
(2,1,7,6,8,4,1,7,2,1),
(6,8,8,2,8,8,1,1,3,4),
(4,8,4,6,8,4,8,5,5,4),
(5,2,8,3,7,5,1,5,2,6)])

arr = np.array([(2,3,4,4,6,7,1,2,1,2),
(6,6,1,1,7,4,2,6,8,1),
(5,5,7,5,5,7,5,5,7,3),
(3,1,6,7,8,4,8,5,3,6),
(1,3,5,3,8,2,7,3,1,1),
(4,4,1,6,4,6,3,2,6,6),
(2,6,2,4,7,6,1,6,1,5),
(1,7,8,6,5,6,1,2,6,3),
(3,6,2,2,6,4,3,2,1,5),
(4,1,4,3,2,8,4,6,5,3)])

total = 0

#for step in range(100):
step = 0
while True:
    currentTotal = 0
    arr += 1

    flashes = np.where(arr == 10)
    while len(flashes[0]) > 0:
        total += len(flashes[0])
        currentTotal += len(flashes[0])

        newrows = []
        newcols = []

        for idx in range(len(flashes[0])):
            r = flashes[0][idx]
            c = flashes[1][idx]

            r1 = max(0, r - 1)
            r2 = min(10, r + 2)
            c1 = max(0, c - 1)
            c2 = min(10, c + 2)

            arr[r1:r2, c1:c2] += 1
            newflashe = np.where(arr[r1:r2, c1:c2] == 10)

            newrows.extend(newflashe[0] + max(0, r - 1))
            newcols.extend(newflashe[1] + max(0, c - 1))

        flashes = [newrows, newcols]

    arr[arr > 9] = 0

    if currentTotal == 100:
        break

    step += 1

