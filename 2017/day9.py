class Group:
    def __init__(self, id, score):
        self.children = []
        self.id = id
        self.score = score

    def __str__(self):
        return f'{self.id} {self.score}'

def score(g):
    s = g.score
    for child in g.children:
        s += score(child)
    return s

stack = []
g = None
idx = 0
id = 1

f = open('input.txt')
input = f.readline()
f.close()

inGarbage = False
gcount = 0

while idx < len(input):
    c = input[idx]

    if c == '!':
        idx += 1

    elif c == '{':
        if not inGarbage:
            if g is not None:
                g2 = Group(id, g.score + 1)
                g.children.append(g2)
                stack.append(g)
                g = g2

            else:
                g = Group(id, 1)
                stack.append(g)

            id += 1
        else:
            gcount += 1

    elif c == '}':
        if not inGarbage:
            g = stack.pop()
        else:
            gcount += 1

    elif c == '<':
        if inGarbage:
            gcount += 1
        inGarbage = True

    elif c == '>':
        inGarbage = False

    else:
        if inGarbage:
            gcount += 1

    idx += 1

print(score(g))
print(gcount)
