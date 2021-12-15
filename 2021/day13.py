import numpy as np

def foldX(x):
    global arr
    print('X', arr.shape[1], x)
    arr2 = arr[:, :x]
    arr3 = np.flip(arr[:, (x+1):], 1)
    arr2 += arr3
    arr = arr2

def foldY(y):
    global arr
    print('Y', arr.shape[0], y)
    arr2 = arr[:y]
    arr3 = np.flip(arr[(y+1):], 0)
    arr2 += arr3
    arr = arr2


rowCount = 0
colCount = 0
dots = []

with open('input.txt') as f:
    for line in f:
        (c, r) = (int(x) for x in line.strip().split(','))
        rowCount = max(rowCount, r+1)
        colCount = max(colCount, c+1)
        dots.append((c, r))

arr = np.zeros((rowCount, colCount), dtype=int)

for dot in dots:
    arr[dot[1], dot[0]] = 1

foldX(655)
foldY(447)
foldX(327)
foldY(223)
foldX(163)
foldY(111)
foldX(81)
foldY(55)
foldX(40)
foldY(27)
foldY(13)
foldY(6)

np.set_printoptions(linewidth=np.inf)
arr[np.where(arr > 1)] = 1
print(arr)
