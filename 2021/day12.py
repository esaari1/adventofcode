count = 0

def dfs(node, stack, d):
    global count
    stack.append(node)

    for e in edges[node]:
        if e == 'end':
            count += 1
            print(stack,'end')

        elif e != 'start':
            if e not in stack or e.isupper():
                dfs(e, stack, d)
            elif not d:
                dfs(e, stack, True)

    stack.pop()


f = open('input.txt')

line = f.readline()

edges = {}

while line:
    (s, e) = line.strip().split('-')
    if s not in edges:
        edges[s] = []
    edges[s].append(e)

    if e not in edges:
        edges[e] = []
    edges[e].append(s)

    line = f.readline()

stack = []
dfs('start', stack, False)

print(count)
