from operator import add
import queue

h = 1
l = 2
vals = [h, l]
names = ['H', 'L']
chips = [h+l,0,0,0]
generators = [0,h,l,0]

# patt 1 data
s = 1
p = 2
t = 4
r = 8
c = 16
e = 32
d = 64
vals = [s, p, t, r, c, e, d]
names = ['S', 'P', 'T', 'R', 'C', 'E', 'D']
chips = [s+p+e+d, r+c, t, 0]
generators = [s+p+e+d, t+r+c, 0, 0]

elevator = 0

combos = vals[:]
i = 0
while i < len(vals) - 1:
    j = i + 1
    while j < len(vals):
        combos.append(vals[i] + vals[j])
        j += 1
    i += 1

maxFloor = len(chips) - 1

class State:
    c = []
    g = []
    e = 0
    step = 0

    def __init__(self, c, g, e):
        self.c = c
        self.g = g
        self.e = e

    def gen_hash(self):
        t = []
        for i in range(len(vals)):
            t.append([0,0])
        t.append([5, self.e])

        for idx, v in enumerate(vals):
            for f in range(len(self.c)):
                if self.c[f] & v == v:
                    t[idx][0] = f
                if self.g[f] & v == v:
                    t[idx][1] = f

        t.sort(key=lambda t: (t[0], t[1]))
        return str(t)
        # return f'{str(self.c)},{str(self.g)},{self.e}'

def printState(c, g, e):
    def gen(f, i):
        return f'{names[i]}G' if g[f] & vals[i] else '.'
    def chip(f, i):
        return f'{names[i]}M' if c[f] & vals[i] else '.'

    f = maxFloor
    sep = '\t'
    while f >= 0:
        print(f'F{f+1}{sep}{"E" if e == f else "."}{"".join(f"{sep}{gen(f, i)}{sep}{chip(f, i)}" for i in range(len(vals)))}')
        f -= 1

endState = State([0,0,0,sum(vals)], [0,0,0,sum(vals)], maxFloor).gen_hash()

def validMoves(state):
    def getMoves(chips, generators, e, tgt):
        moves = []
        pair = False

        for v in combos:
            genOnFloor = (generators[e] & v) == v
            if (chips[e] & v) == v: # is chip on floor
                uncoveredChips = chips[e + tgt] & generators[e + tgt] != chips[e + tgt]

                if genOnFloor and not uncoveredChips: # generator on floor and no uncovered chips
                    if v in vals and not pair: # if single chip
                        moves.append((tgt, v, v)) # can move chip and generator
                        pair = True
                if ((generators[e + tgt] & v) == v) or (generators[e + tgt] == 0): # if generator on target or no generators on target
                    moves.append((tgt, v, 0)) # can move chip

            if genOnFloor: # generator on floor
                uncoveredChips = (chips[e + tgt] - v) & (generators[e + tgt] - v) != (chips[e + tgt] - v)

                if not uncoveredChips: # if chip on target and no other uncovered chips on target
                    moves.append((tgt, 0, v)) # can move generator

        return moves

    moves = []

    sums = list(map(add, state.c, state.g))
    minfloor = min( i for i,f in enumerate(sums) if f )

    if state.e < maxFloor:
        moves.extend(getMoves(state.c, state.g, state.e, 1))
    if state.e > 0 and (state.e - 1) >= minfloor:
        moves.extend(getMoves(state.c, state.g, state.e, -1))

    return moves

def applyMove(state, move):
    c = state.c[:]
    c[state.e] -= move[1]
    c[state.e + move[0]] += move[1]
    g = state.g[:]
    g[state.e] -= move[2]
    g[state.e + move[0]] += move[2]
    return State(c, g, state.e + move[0])

def bfs(root):
    tree = {}
    tree[root] = True
    step = 0

    q = queue.Queue()

    q.put(root)

    while not q.empty():
        v =  q.get()
        vh = v.gen_hash()

        if vh == endState:
            print(v.step)
            exit()

        moves = validMoves(v)
        # printState(v.c, v.g, v.e)
        # print(moves)

        for move in moves:
            state = applyMove(v, move)
            state.step = v.step + 1
            stateh = state.gen_hash()

            if stateh not in tree:
                tree[stateh] = True
                q.put(state)

start = State(chips, generators, elevator)
bfs(start)

# for each chip
#     if on floor
#         if generator on floor and no uncovered chips on target
#             if single chip
#                 can move chip and generator
#         if generator on target or no generators on target
#             can move chip

# for each generator
#     if on floor
#         REPEAT
#         if chip on floor  and no uncovered chips on target
#             if single generator
#                 can move chip and generator
#         if chip on target and no uncovered chips on target
#             can move generator
