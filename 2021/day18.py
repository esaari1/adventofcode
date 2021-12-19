from math import floor, ceil

class Node:
    def __init__(self, depth, p, val = None):
        self.depth = depth
        self.parent = p
        self.val = val
        self.left = None
        self.right = None

    def print(self):
        print('   '*self.depth, '[', self.depth, ']', self.val)
        if self.left:
            self.left.print()
        if self.right:
            self.right.print()

    def toString(self):
        if self.val is not None:
            return self.val

        return f'[{self.left.toString()}, {self.right.toString()}]'

    def isVal(self):
        return self.val is not None

    def explode(self):
        global top
        taken = False

        if self.depth >= 4 and self.left and self.right and self.left.isVal() and self.right.isVal():
            # explode
            self.val = 'X'

            s = top.toString()
            xidx = s.index('X')
            lidx = xidx - 1
            while lidx >= 0 and s[lidx] in ('[', ']', ',', ' '):
                lidx -= 1

            if lidx >= 0:
                lidx2 = lidx - 1
                while lidx2 >= 0 and s[lidx2] not in ('[', ']', ',', ' '):
                    lidx2 -= 1
                v = int(s[lidx2+1:lidx+1]) + self.left.val
                s = f'{s[:lidx2+1]}{v}{s[lidx+1:]}'

            xidx = s.index('X')
            ridx = xidx + 1
            while ridx < len(s) and s[ridx] in ('[', ']', ',', ' '):
                ridx += 1

            if ridx < len(s):
                ridx2 = ridx + 1
                while ridx2 < len(s) and s[ridx2] not in ('[', ']', ',', ' '):
                    ridx2 += 1
                v = int(s[ridx:ridx2]) + self.right.val
                s = f'{s[:ridx]}{v}{s[ridx2:]}'

            s = s.replace('X', '0')
            s = eval(s)
            top = Node(0, None)
            buildTree(s, top)
            return True

        if self.left:
            taken = self.left.explode()

        if self.right and not taken:
            taken = self.right.explode()

        return taken

    def split(self):
        taken = False
        if self.val is not None and self.val >= 10:
            # split
            self.left = Node(self.depth + 1, self, int(floor(self.val / 2)))
            self.right = Node(self.depth + 1, self, int(ceil(self.val / 2)))
            self.val = None
            return True

        if self.left and not taken:
            taken = self.left.split()

        if self.right and not taken:
            taken = self.right.split()

        return taken

    def magnitude(self):
        if self.left and self.right:
            if self.left.isVal() and self.right.isVal():
                return self.left.val * 3 + self.right.val * 2
            elif self.left.isVal():
                return 3 * self.left.val + 2 * self.right.magnitude()
            elif self.right.isVal():
                return 3 * self.left.magnitude() + 2 * self.right.val
            else:
                return 3 * self.left.magnitude() + 2 * self.right.magnitude()



def buildTree(l, parent):
    if type(l) is list:
        leftChild = Node(parent.depth + 1, parent)
        parent.left = leftChild
        buildTree(l[0], leftChild)

        rightChild = Node(parent.depth + 1, parent)
        parent.right = rightChild
        buildTree(l[1], rightChild)
    else:
        parent.val = l


def part1():
    f = open('input.txt')

    l = f.readline()
    l = eval(l.strip())
    l2 = f.readline()

    while l2:
        l2 = eval(l2.strip())
        l = [l, l2]
        print(l)

        top = Node(0, None)
        buildTree(l, top)

        #top.print()
        action = True
        while action:
            action = top.explode()
            if not action:
                action = top.split()

        l = eval(top.toString())
        print(top.toString())
        l2 = f.readline()

    print(top.toString())

    # l = [[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]
    # top = Node(0, None)
    # buildTree(l, top)
    print(top.magnitude())

    f.close()

top =  None
def part2():
    global top
    f = open('input.txt')

    lists = []
    line = f.readline()

    while line:
        l = eval(line.strip())
        lists.append(l)
        line = f.readline()

    f.close()

    ans = 0
    for idx1 in range(len(lists) - 1):
        for idx2 in range(idx1 + 1, len(lists)):
            l = [lists[idx1], lists[idx2]]
            top = Node(0, None)
            buildTree(l, top)

            #top.print()
            action = True
            while action:
                action = top.explode()
                if not action:
                    action = top.split()

            m = top.magnitude()
            if m > ans:
                ans = m

            l = [lists[idx2], lists[idx1]]
            top = Node(0, None)
            buildTree(l, top)

            #top.print()
            action = True
            while action:
                action = top.explode()
                if not action:
                    action = top.split()

            m = top.magnitude()
            if m > ans:
                ans = m
    print(ans)

part2()
