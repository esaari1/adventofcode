import queue, copy

class Node:
    def __init__(self, s = 0, u = 0):
        self.size = s
        self.used = u

    def avail(self):
        return self.size - self.used

    def __str__(self):
        return f'{self.used}/{self.size}'

def coords(node):
    p = node.split('-')
    return (int(p[1][1:]), int(p[2][1:]))

def moveCheck(v2, x, y, x2, y2, tgt, move):
    n = at(v2, x, y)
    n2 = at(v2, x2, y2)
    if n.avail() >= n2.used and n2.used > 0:
        n.used += n2.used
        n2.used = 0

        if (x2, y2) == tgt:
            return (v2, (x,y), move, x2, y2)
        return (v2, tgt, move, x2, y2)
    return False

def validMoves(x, y, v, tgt, move):
    result = []
    # for y in range(sizey):
    #     for x in range(sizex):
    if x > 0:
        v2 = copy.deepcopy(v)
        m = moveCheck(v2, x, y, x-1, y, tgt, move)
        if m:
            result.append(m)

    if x < sizex-1:
        v2 = copy.deepcopy(v)
        m = moveCheck(v2, x, y, x+1, y, tgt, move)
        if m:
            result.append(m)

    if y > 0:
        v2 = copy.deepcopy(v)
        m = moveCheck(v2, x, y, x, y-1, tgt, move)
        if m:
            result.append(m)

    if y < sizey-1:
        v2 = copy.deepcopy(v)
        m = moveCheck(v2, x, y, x, y+1, tgt, move)
        if m:
            result.append(m)


    return result

def setup(arr):
    s = ''
    for a in arr[0]:
        s += str(a)
    s += str(arr[1])
    return s

def bfs(arr, check):
    visited = {}
    m = (arr, (sizex-1, 0), 0, check[0], check[1])
    visited[setup(m)] = True
    q = queue.Queue()

    q.put(m)

    while not q.empty():
        v =  q.get()
        print('START ', v[1], v[2])
        state(v[0])

        if v[1] == (0, 0):
            print('DONE ', v[2])
            exit(0)


        moves = validMoves(v[3], v[4], v[0], v[1], v[2]+1)
        for m in moves:
            sm = setup(m)
            if sm not in visited:
                # print('M ', m[1])
                # state(m[0])

                visited[sm] = True
                q.put(m)

def at(arr, x, y):
    return arr[y * sizex + x]

def state(arr):
    for y in range(sizey):
        for x in range(sizex):
            print(at(arr, x, y), end='\t')
        print()
    print()

f = open('input.txt')
lines = f.readlines()
f.close()

node = lines[-1].split(' ')[0]

sizex, sizey = coords(node)
sizex += 1
sizey += 1
arr = [Node] * sizex * sizey

check = ()
for l in lines:
    p = l.strip().split()
    if p[0] == 'Filesystem':
        continue

    x, y = coords(p[0])
    arr[y * sizex + x] = Node(int(p[1][:-1]), int(p[2][:-1]))
    if arr[y * sizex + x].used == 0:
        check = (x, y)

# print(check)

# bfs(arr, check)
state(arr)
print(check)