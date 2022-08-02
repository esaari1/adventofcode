def part1():
    arr = [0, 1]
    pos = 1
    step = 356

    for i in range(1, 2017):
        pos = (pos + 1 + step) % len(arr)
        arr.insert(pos, (i+1))

    print(arr[pos+1])

# part 2
from collections import deque

puzzle = 356
spinlock = deque([0])

for i in range(1, 50000001):
    spinlock.rotate(-puzzle)
    spinlock.append(i)

print(spinlock[spinlock.index(0) + 1])
