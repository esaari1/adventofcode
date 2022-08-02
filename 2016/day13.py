import queue

dx = 31
dy = 39
input = 1350

# dx = 7
# dy = 4
# input = 10

def is_open(x, y):
    if x < 0 or y < 0:
        return False
    n = x*x + 3*x + 2*x*y + y + y*y + input
    return bin(n).count("1") % 2 == 0

def validMoves(pos):
    moves = []
    if is_open(pos[0] - 1, pos[1]):
        moves.append((pos[0] - 1, pos[1]))
    if is_open(pos[0] + 1, pos[1]):
        moves.append((pos[0] + 1, pos[1]))
    if is_open(pos[0], pos[1] - 1):
        moves.append((pos[0], pos[1] - 1))
    if is_open(pos[0], pos[1] + 1):
        moves.append((pos[0], pos[1] + 1))

    return moves

def part1(v):
    if v[0] == dx and v[1] == dy:
        print(v[2])
        exit()

def part2(v):
    return v[2] == 50

visited = {}

def bfs():
    global visited
    q = queue.Queue()

    visited[(1, 1)] = True
    q.put((1, 1, 0))

    while not q.empty():
        v =  q.get()

        # part1(v)
        if part2(v):
            return

        moves = validMoves(v)
        for m in moves:
            if m not in visited:
                visited[m] = True
                q.put((m[0], m[1], v[2] + 1))

bfs()
print(len(visited))
