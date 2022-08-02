class Node:
    def __init__(self, c):
        self.n = None
        self.s = None
        self.e = None
        self.w = None
        self.c = c

    def __str__(self):
        return self.c

nodes = []
currNode = None
prevCache = {}
cache = {}

with open('input.txt') as f:
    line = f.readline()

    while line:
        #print(line[:-1])
        pos = 0

        prevC = ''
        prevN = None

        for c in line[:-1]:
            if c == ' ':
                prevN = None

            else:
                node = Node(c)
                if currNode is None:
                    currNode = node
                nodes.append(node)

                if pos in prevCache and (node.c in ['|', '+'] or prevCache[pos].c in ['|', '+'] or prevCache[pos].n is not None):
                    prevCache[pos].s = node
                    node.n = prevCache[pos]
                cache[pos] = node

                if prevN is not None and ((c == '-' or c == '+' or c.isalpha()) or (prevC == '-' or prevC == '+' or prevC.isalpha())):
                    #if prevC == '-' or prevC == '+' or prevC.isalpha():
                    prevN.e = node
                    node.w = prevN

                prevC = c
                prevN = node

            pos += 1

        prevCache = cache.copy()
        cache = {}

        line = f.readline()

#print(currNode.n, currNode.s, currNode.e, currNode.w)
ans = ''

N = 0
S = 1
W = 2
E = 3

prevDir = S
step = 0

while True:
    step += 1
    if currNode.c.isalpha():
        ans += currNode.c

#    print(prevDir, currNode.c)

    if prevDir == N:
        if currNode.n is not None:
            currNode = currNode.n
        elif currNode.w is not None:
            currNode = currNode.w
            prevDir = W
        elif currNode.e is not None:
            currNode = currNode.e
            prevDir = E
        else:
            print(ans, step)
            exit(0)

    elif prevDir == S:
        if currNode.s is not None:
            currNode = currNode.s
        elif currNode.w is not None:
            currNode = currNode.w
            prevDir = W
        elif currNode.e is not None:
            currNode = currNode.e
            prevDir = E
        else:
            print(ans, step)
            exit(0)

    elif prevDir == W:
        if currNode.w is not None:
            currNode = currNode.w
        elif currNode.n is not None:
            currNode = currNode.n
            prevDir = N
        elif currNode.s is not None:
            currNode = currNode.s
            prevDir = S
        else:
            print(ans, step)
            exit(0)

    elif prevDir == E:
        if currNode.e is not None:
            currNode = currNode.e
        elif currNode.n is not None:
            currNode = currNode.n
            prevDir = N
        elif currNode.s is not None:
            currNode = currNode.s
            prevDir = S
        else:
            print(ans, step)
            exit(0)
