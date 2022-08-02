import hashlib
import queue

input = 'ulqzkmiv'
input = 'pxxbnzuo'
open = ['b', 'c', 'd', 'e', 'f']

max = 0

def bfs():
    global max

    q = queue.Queue()
    # path, step, x, y
    q.put(('', 0, 0, 0))

    while not q.empty():
        v =  q.get()

        if v[2] == 3 and v[3] == 3:
            # part 1
            # print(v[0], v[1])
            # exit()

            # part 2
            if max < v[1]:
                max = v[1]
            continue

        hash = hashlib.md5((input + v[0]).encode('utf-8')).hexdigest()[:4]

        if hash[0] in open and v[3] > 0: # up
            q.put((v[0] + 'U', v[1] + 1, v[2], v[3] - 1))

        if hash[1] in open and v[3] < 3: #down
            q.put((v[0] + 'D', v[1] + 1, v[2], v[3] + 1))

        if hash[2] in open and v[2] > 0: #left
            q.put((v[0] + 'L', v[1] + 1, v[2] - 1, v[3]))

        if hash[3] in open and v[2] < 3: #right
            q.put((v[0] + 'R', v[1] + 1, v[2] + 1, v[3]))

bfs()
print(max)
