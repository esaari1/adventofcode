import numpy as np
import sys
import time

from bisect import bisect_left

sys.setrecursionlimit(15000)

size = 100
scale = 5
arr = np.zeros((size*scale, size*scale), dtype = int)

class PriorityQueue:
    def __init__(self):
        self.keys = []
        self.vals = []

    def add(self, k, v):
        if len(self.keys) == 0:
            self.keys.append(k)
            self.vals.append(v)

        else:
            idx = bisect_left(self.vals, v)
            self.keys.insert(idx, k)
            self.vals.insert(idx, v)

    def has(self, k):
        return k in self.keys

    def empty(self):
        return len(self.keys) == 0

    def pop(self):
        k = self.keys[0]
        self.keys = self.keys[1:]
        self.vals = self.vals[1:]
        return k

def path(cameFrom, current):
    total = arr[current]
    while current in cameFrom:
        current = cameFrom[current]
        total += arr[current]

    print(total - arr[0,0])

def astar(start):
    startT = time.time()

    k = PriorityQueue()
    k.add(start, (maxR + maxC) )

    gscore = {}
    gscore[(0, 0)] = 0
    cameFrom = {}

    while not k.empty():
        pos = k.pop()
        if pos == (maxR, maxC):
            path(cameFrom, pos)
            end = time.time()
            print(end - startT)

            exit(0)

        moves = []

        # move right
        if pos[1] < maxC:
            moves.append((pos[0], pos[1] + 1))

        # move down
        if pos[0] < maxR:
            moves.append((pos[0] + 1, pos[1]))

        # move left
        if pos[1] > 0:
            moves.append((pos[0], pos[1] - 1))

        # move up
        if pos[0] > 0:
            moves.append((pos[0] - 1, pos[1]))

        for move in moves:
            tentative_gscore = gscore.get(pos, 100000000) + arr[move[0], move[1]]
            if tentative_gscore < gscore.get(move, 100000000):
                cameFrom[move] = pos
                gscore[move] = tentative_gscore
                if not k.has(move):
                    #k[move] = tentative_gscore + (maxR - move[0]) + (maxC - move[1]) * 1
                    k.add(move, tentative_gscore + (maxR - move[0]) + (maxC - move[1]) * 1)


with open('input.txt') as f:
    row = 0
    for line in f:
        col = 0
        for c in line.strip():
            val = int(c)
            for x in range(scale):
                for y in range(scale):
                    v = val + x + y
                    if v >= 10:
                        v = v - 9
                    arr[row+(y*size), col+(x*size)] = v
            col += 1
        row += 1

maxR = arr.shape[0] - 1
maxC = arr.shape[1] - 1

astar((0, 0))
